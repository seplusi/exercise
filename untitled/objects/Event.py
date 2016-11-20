class Event(object):
    """
        Class with the event data
    """
    def __init__(self, peril, region, damage, deals_db):
        """
            Doc

        :param peril: String with peril
        :param region: String with region
        :param damage: Integer with damage value
        :param deals_db: Dictionary with all deals. Since there's no database to query I had to pass all data to the obj
        """
        self.peril = peril
        self.region = region
        self.damage = damage
        self.deals_list = []
        self.get_applicable_deals(deals_db)

    def get_applicable_deals(self, deals_db):
        """
            Method that retrieves all applicable deals to this event

        :param deals_db: Dictionary with all deals. Since there's no database I had to pass all data to the obj
        :return: List with all applicable existing deals
        """
        list_deals = []
        for key in deals_db.keys():
            if self.region in deals_db[key]['regions'] and self.peril in deals_db[key]['perils']:
                list_deals.append(deals_db[key])

        self.deals_list = list_deals

    def total_loss(self):
        """
            Method that calculates the total loss caused by the event based in existing deals

        :return: Integer with total loss
        """
        loss = 0
        if not self.deals_list:
            print "No applicable deal exists."
        else:
            for deal in self.deals_list:
                if deal['retention'] < self.damage and deal['retention'] + deal['limit'] >= self.damage:
                    loss = loss + self.damage - deal['retention']
                elif deal['retention'] + deal['limit'] < self.damage:
                    loss = loss + deal['limit']

        return loss
