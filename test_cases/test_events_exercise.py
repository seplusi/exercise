from unittest import TestCase
from objects.ManageDeals import ManageDeals
from objects.Event import Event

deals = {'deal1': {'retention': 100, 'limit': 500, 'perils': ['earthquake'], 'regions': ['California']},
         'deal2': {'retention': 1000, 'limit': 3000, 'perils': ['hurricane'], 'regions': ['Florida']},
         'deal3': {'retention': 250, 'limit': 250, 'perils': ['hurricane', 'flood'],
                   'regions': ['Florida', 'Louisiana']}
         }

"""
To run the functional tests:
# nosetests -v {project path}/test_cases/test_events_exercise.py  --tc-format python --nologcapture
"""


class TestEventsExercise(TestCase):

    def test_calculate_loss_event4(self):
        """
            Tests that event4 causes a loss of 1250. Tests when an event affects more than 1 deal.
        """
        event = Event('hurricane', 'Florida', 2000, deals)
        loss = event.total_loss()
        assert loss == 1250

    def test_calculate_loss_event2(self):
        """
            Tests that event2 causes a loss of 250
        """
        event = Event('flood', 'Louisiana', 500, deals)
        loss = event.total_loss()
        assert loss == 250

    def test_calculate_loss_event3(self):
        """
            Tests that event3 causes a loss of 250
        """
        event = Event('flood', 'Florida', 750, deals)
        loss = event.total_loss()
        assert loss == 250

    def test_calculate_loss_event1(self):
        """
            Tests that event1 causes a loss of 500
        """
        event = Event('earthquake', 'California', 1000, deals)
        loss = event.total_loss()
        assert loss == 500

    def test_add_new_deal_and_calculate_loss(self):
        """
            Tests that a new deal can be added dynamically for an uncovered event and the loss can be calculated on the
            fly
        """
        peril = 'fire'
        region = 'Porto'
        damage = 400
        event = Event(peril, region, damage, deals)
        if not event.deals_list:
            ManageDeals.add_new_deal(250, 250, [peril, ], [region, ], deals)
            event.get_applicable_deals(deals)

        loss = event.total_loss()

        assert loss == 150

    def test_add_new_region_to_existing_deal_and_calculate_loss(self):
        """
            Tests that a new region can be added dynamically to an existing deal for an uncovered event and the loss
            can be calculated on the fly
        """
        peril = 'fire'
        region = 'Porto'
        damage = 400
        event = Event(peril, region, damage, deals)
        if not event.deals_list:
            ManageDeals.add_new_deal(250, 250, [peril, ], [region, ], deals)

        peril = 'fire'
        region = 'Lisbon'
        damage = 700
        event = Event(peril, region, damage, deals)
        if not event.deals_list:
            ManageDeals.add_region_to_deal('deal4', region, deals)
            event.get_applicable_deals(deals)

        loss = event.total_loss()

        assert loss == 250

    def test_add_new_peril_to_existing_deal_and_calculate_loss(self):
        """
            Tests that a new peril can be added dynamically to an existing deal for an uncovered event and the loss
            can be calculated on the fly. Also tests that is the damage is lower then the retention, then the loss is 0
        """
        peril = 'fire'
        region = 'Porto'
        damage = 400
        event = Event(peril, region, damage, deals)
        if not event.deals_list:
            ManageDeals.add_new_deal(250, 250, [peril, ], [region, ], deals)

        peril = 'fire'
        region = 'Lisbon'
        damage = 700
        event = Event(peril, region, damage, deals)
        if not event.deals_list:
            ManageDeals.add_region_to_deal('deal4', region, deals)

        peril = 'draught'
        region = 'Lisbon'
        damage = 100
        event = Event(peril, region, damage, deals)
        if not event.deals_list:
            ManageDeals.add_peril_to_deal('deal4', peril, deals)
            event.get_applicable_deals(deals)

        loss = event.total_loss()

        assert loss == 0
