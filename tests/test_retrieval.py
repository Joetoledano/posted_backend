import unittest
from util.db_util import get_deals

class TestRetrieval(unittest.TestCase):

    def test_retrieval(self):
        get_deals()
