class ManageDeals(object):
    """
        Class that manages deals
    """
    @classmethod
    def add_new_deal(self, retention, limit, perils, regions, deals_db):
        """
            Adds a new deal to the deals dictionary

        :param retention: Integer with retention value
        :param limit: Integer with limit value
        :param perils: List of strings with perils
        :param regions: List of strings with regions
        :param deals_db: Dictionary with all deals
        :return: None
        """
        deal_id = len(deals_db.keys()) + 1
        deals_db['deal%s' % deal_id] = {'retention': retention, 'limit': limit, 'perils': perils, 'regions': regions}

    @classmethod
    def add_region_to_deal(self, deal, new_region, deals_db):
        """
            Adds a region to an existing deal

        :param deal: String with existing deal
        :param new_region: String with new region name
        :param deals_db: Dictionary with all deals
        :return: None
        """
        deals_db[deal]['regions'].append(new_region)

    @classmethod
    def add_peril_to_deal(self, deal, new_peril, deals_db):
        """
            Adds a peril to an existing deal

        :param deal: String with existing deal
        :param new_peril: String with new peril name
        :param deals_db: Dictionary with all deals
        :return: None
        """
        deals_db[deal]['perils'].append(new_peril)