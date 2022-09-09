import unittest
import sys
import io
from unittest.mock import patch
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.cache_reader import RssCacher  # noqa: E402


class TestRssCacher(unittest.TestCase):

    def setUp(self):
        self.config = {'source': 'a', 'limit': 2, 'date': "00000001",
                       'scenario': 'scenario 2: get news from cache with limit or without limit',
                       'to_html': False, 'to_pdf': False, 'path_for_html': 'rss_reader.html',
                       'path_for_pdf': 'rss_reader.pdf', 'publish_date': '00000001'}
        self.path_cache = str(Path(__file__).parents[1].joinpath('tests', 'rss_cache.json'))
        self.rss_cacher = RssCacher(self.config, self.path_cache)

    def test__parse_response(self):
        self.rss_cacher.response = {}
        self.rss_cacher.cash = []
        self.assertEqual(str(self.rss_cacher.cash), '[]')
        self.rss_cacher._parse_response()
        self.assertEqual(str(self.rss_cacher.cash)[:16], "[{'00000001': {'")

    def test_get_limit(self):
        self.assertEqual(self.rss_cacher.limit, 2)
        self.rss_cacher.cash = []
        self.rss_cacher._parse_response()
        self.config['limit'] = 100
        self.assertEqual(self.rss_cacher.get_limit(), 3)
        self.rss_cacher.cash = []
        self.rss_cacher._parse_response()
        self.config['limit'] = False
        self.assertEqual(self.rss_cacher.get_limit(), 3)

    def test__limiting_cache(self):
        self.rss_cacher.cash = []
        self.rss_cacher.cash_json = []
        self.rss_cacher.cache_limited = []
        self.rss_cacher.cache_json_limited = []
        self.assertEqual(str(self.rss_cacher.cache_json_limited), '[]')
        self.rss_cacher.limit = 2
        self.rss_cacher._parse_response()
        self.rss_cacher._limiting_cache()
        self.assertEqual(len(self.rss_cacher.cache_json_limited), 234)
        self.rss_cacher.cash = []
        self.rss_cacher.cash_json = []
        self.rss_cacher.cache_limited = []
        self.rss_cacher.cache_json_limited = []
        self.rss_cacher.limit = 1
        self.rss_cacher._parse_response()
        self.rss_cacher._limiting_cache()
        self.assertEqual(len(self.rss_cacher.cache_json_limited), 117)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_rss(self, mock_stdout):
        self.rss_cacher.cache_limited = []
        self.rss_cacher.cache_json_limited = []
        self.rss_cacher.config['json'] = False
        self.rss_cacher._limiting_cache()
        self.rss_cacher.print_rss()
        self.assertEqual(str(mock_stdout.getvalue())[:55], "\n********** DATA FROM CACHE **********\n\n\nFeed: "
                                                           "feed_a\n\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_rss_json(self, mock_stdout):
        self.rss_cacher.cache_limited = []
        self.rss_cacher.cache_json_limited = []
        self.rss_cacher.config['json'] = True
        self.rss_cacher._limiting_cache()
        self.rss_cacher.print_rss()
        self.assertEqual(str(mock_stdout.getvalue())[:55], "\n********** DATA FROM CACHE **********\n\n[\n    "
                                                           "{\n       ")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_rss_error(self, mock_stdout):
        self.rss_cacher.cash = []
        self.rss_cacher.print_rss()
        self.assertEqual(mock_stdout.getvalue(), "\n********** DATA FROM CACHE **********\n\nNot news for this date\n")


if __name__ == '__main__':
    unittest.main()
