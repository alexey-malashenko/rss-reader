import unittest
import feedparser
import sys
import io
from unittest.mock import patch
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.rss_parser import Rss  # noqa: E402


config = {'source': 'http://rss.cnn.com/rss/edition_world.rss', 'json': True, 'verbose': True, 'limit': 5,
          'datetime': 'Fri, 02 Sep 2022 21:37:05 +0000'}
sys.path.append(str(Path(__file__)))
response = feedparser.parse('edition_world.xml')
new_response = feedparser.parse('input.xml')
add_response = feedparser.parse('input_2.xml')
path_cache = str(Path(__file__).parents[1].joinpath('src', 'main_reader', 'cache', 'rss_cache.json'))

cache = {'20220902': {
    'Feed': 'CNN.com - RSS Channel - World',
    'Title': "Argentina's Vice President Kirchner threatened with gun outside her home",
    'Date': 'Fri, 02 Sep 2022 14:52:26 +0000',
    'Link': 'https://www.cnn.com/2022/09/01/americas/argentina-cristina-fernndez-de-kirchner-gun-intl-hnk/index.html',
    'Links': [
        '[1]: https://www.cnn.com/2022/09/01/americas/argentina-cristina-fernndez-de-kirchner-gun-intl-hnk/index.html '
        '(link)']}}


class TestRss(unittest.TestCase):
    def setUp(self):
        self.rss = Rss
        self.config = config
        self.response = response
        self.path_cache = path_cache
        self.cache = cache


class TestInit(TestRss):
    def test_initial_response(self):
        self.assertEqual(self.rss(self.response, self.config, self.path_cache).response, response)

    def test_initial_config(self):
        self.assertEqual(self.rss(self.response, self.config, self.path_cache).config, config)

    def test_initial_limit(self):
        self.assertEqual(self.rss(self.response, self.config, self.path_cache).limit,
                         self.rss(self.response, self.config, self.path_cache).limit)

    def test_initial_path_cache(self):
        self.assertEqual(self.rss(self.response, self.config, self.path_cache).path_cache, self.path_cache)


class TestLimit(TestRss):
    def test_limit(self):
        self.rss_a = Rss(response, config, path_cache)
        self.assertEqual(self.rss_a.get_limit(), self.rss_a.get_limit())

    def test_limit_conf(self):
        self.rss_a = Rss(response, config, path_cache)
        self.rss_a.config['limit'] = 2
        self.rss_a.response['entries'] = [{"1": 2}, {"2": 2}, {"3": 2}, {"4": 2}, {"5": 2}]
        self.assertEqual(self.rss_a.get_limit(), 2)


class TestParseResponseCash(TestRss):
    def test_parse_response_cash_type(self):
        self.rss_b = Rss(new_response, config, path_cache)
        self.rss_b.config['limit'] = 1
        self.rss_b.parse_response()
        self.assertTrue(type(self.rss_b.cash), [])


class TestPrintRss(TestRss):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_rss(self, mock_stdout):
        self.rss_o = Rss(new_response, config, path_cache)
        self.rss_o.cache_limited = []
        self.rss_o.cache_json_limited = []
        self.rss_o.config['json'] = False
        self.rss_o.print_rss()
        self.assertEqual(str(mock_stdout.getvalue())[:36], "\n********** DATA FROM URL **********")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_rss_error(self, mock_stdout):
        self.rss_o = Rss(new_response, config, path_cache)
        self.config['json'] = False
        self.rss_o.cash = []
        self.rss_o.print_rss()
        self.assertEqual(mock_stdout.getvalue(), "\n********** DATA FROM URL **********\n\n")
