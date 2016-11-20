import sys
import unittest2
from objects.Event import Event

"""
Execute unit tests
# PYTHONPATH={project_path}
# python unit_tests/u_tests_event.py

"""


deals = {'deal1': {'retention': 100, 'limit': 500, 'perils': ['earthquake'], 'regions': ['California']},
         'deal2': {'retention': 1000, 'limit': 3000, 'perils': ['hurricane'], 'regions': ['Florida']},
         'deal3': {'retention': 250, 'limit': 250, 'perils': ['hurricane', 'flood'],
                   'regions': ['Florida', 'Louisiana']}
         }


class EventUnitTests(unittest2.TestCase):

    def test_get_applicable_deals_returns_list_with_1_deal(self):
        event = Event('flood', 'Louisiana', 500, deals)
        event.deals_list = []
        event.get_applicable_deals(deals)
        self.assertAlmostEqual(event.deals_list, [{'retention': 250, 'limit': 250, 'perils': ['hurricane', 'flood'],
                                     'regions': ['Florida', 'Louisiana']}])

    def test_get_applicable_deals_returns_list_with_2_deal(self):
        event = Event('hurricane', 'Florida', 2000, deals)
        event.deals_list = []
        event.get_applicable_deals(deals)
        self._baseAssertEqual(event.deals_list, [{'regions': ['Florida', 'Louisiana'], 'perils': ['hurricane', 'flood'],
                                     'limit': 250, 'retention': 250}, {'regions': ['Florida'], 'perils': ['hurricane'],
                                                                       'limit': 3000, 'retention': 1000}])

    def test_get_applicable_deals_returns_empty_list_when_there_is_no_deal_for_event(self):
        event = Event('hurricane', 'Minnesota', 2000, deals)
        event.deals_list = ['dummy data']
        event.get_applicable_deals(deals)
        self._baseAssertEqual(event.deals_list, [])

    def test_total_loss_returns_0_when_no_deal_exists_for_event(self):
        event = Event('hurricane', 'Minnesota', 2000, deals)
        event.deals_list = []
        self.assertTrue(event.total_loss() == 0)

    def test_total_loss_returns_0_when_damage_lower_then_retention(self):
        event = Event('flood', 'Louisiana', 100, deals)
        self.assertTrue(event.total_loss() == 0)

    def test_total_loss_lower_then_limit(self):
        event = Event('flood', 'Louisiana', 450, deals)
        self.assertTrue(event.total_loss() == 200)

    def test_total_loss_limited_by_limit(self):
        event = Event('flood', 'Louisiana', 450000, deals)
        self.assertTrue(event.total_loss() == 250)

    def test_total_loss_limited_by_limit(self):
        event = Event('flood', 'Louisiana', 450000, deals)
        self.assertTrue(event.total_loss() == 250)

    def test_total_loss_returns_0_with_several_deals_when_damage_lower_the_retetion(self):
        event = Event('hurricane', 'Florida', 50, deals)
        self.assertTrue(event.total_loss() == 0)

    def test_total_loss_returns_0_with_several_deals_when_damage_lower_the_retetion(self):
        event = Event('hurricane', 'Florida', 50, deals)
        self.assertTrue(event.total_loss() == 0)

    def test_total_loss_returns_limit_from_1st_deal_when_damage_higher_then_limit(self):
        event = Event('hurricane', 'Florida', 600, deals)
        self.assertTrue(event.total_loss() == 250)

    def test_total_loss_when_damage_higher_then_deal3_limit_but_lower_then_deal2_limit(self):
        event = Event('hurricane', 'Florida', 2000, deals)
        self.assertTrue(event.total_loss() == 1250)

    def test_total_loss_when_damage_higher_then_deal3_limit_and_deal2_limit(self):
        event = Event('hurricane', 'Florida', 5000, deals)
        self.assertTrue(event.total_loss() == 3250)

if __name__ == "__main__":
    suite = unittest2.TestLoader().loadTestsFromTestCase(EventUnitTests)
    result = unittest2.TextTestRunner(verbosity=2).run(suite)

    if not result.wasSuccessful():
        sys.exit(1)