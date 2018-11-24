import unittest
from oblib import Taxonomy

tax = Taxonomy()

class TestTaxonomy(unittest.TestCase):

    def test_element(self):
        self.assertEqual(tax.check(), "Works")
