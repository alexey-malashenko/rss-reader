import unittest
import feedparser
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.rss_parser import Rss  # noqa: E402


config = {'source': 'http://rss.cnn.com/rss/edition_world.rss', 'json': True, 'verbose': True, 'limit': 5,
          'datetime': 'Fri, 02 Sep 2022 21:37:05 +0000'}
sys.path.append(str(Path(__file__)))
response = feedparser.parse('edition_world.xml')

cash = {'20220902': {
    'Feed': 'CNN.com - RSS Channel - World', 'Title': "Argentina's Vice President Kirchner threatened with gun "
                                                      "outside her home",
    'Date': 'Fri, 02 Sep 2022 14:52:26 +0000',
    'Link': 'https://www.cnn.com/2022/09/01/americas/argentina-cristina-fernndez-de-kirchner-gun-intl-hnk/index.html',
    'Links': [
        '[1]: https://www.cnn.com/2022/09/01/americas/argentina-cristina-fernndez-de-kirchner-gun-intl-hnk/index.html '
        '(link)']}}


class TestRss(unittest.TestCase):
    def setUp(self):
        self.rss = Rss(response, config)


class TestInit(TestRss):
    def test_initial_response(self):
        self.assertEqual(self.rss.response, response)

    def test_initial_config(self):
        self.assertEqual(self.rss.config, config)

    def test_initial_limit(self):
        self.assertEqual(self.rss.limit, 5)


class TestRssLimit(unittest.TestCase):
    def setUp(self):
        config['limit'] = 50
        self.rss = Rss(response, config)


class TestLimit(TestRssLimit):
    def test_limit(self):
        self.assertEqual(self.rss.get_limit(), 29)


class TestRssParser(unittest.TestCase):
    def setUp(self):
        config['limit'] = 1
        self.rss = Rss(response, config)


class TestParseResponseCash(TestRssParser):
    def test_parse_response_cash_type(self):
        self.assertTrue(type(self.rss.cash), [])

    def test_parse_response_cash_not_empty(self):
        self.assertTrue(self.rss.cash.count(cash), 0)
        self.assertTrue(cash in self.rss.cash, True)


class TestParseResponseCashJson(TestRssParser):
    def test_parse_response_cash_json_type(self):
        self.assertTrue(type(self.rss.cash_json), 'str')
