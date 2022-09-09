import unittest
import argparse
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.config import get_config  # noqa: E402


args = argparse.ArgumentParser(prog='rss-reader', description="Pure python command-line RSS reader")
args.add_argument('source', help='RSS URL', nargs='?', default='http://rss.cnn.com/rss/edition_world.rss')
args.add_argument('--json', help='Print result as JSON in stdout', action='store_true', default=True)
args.add_argument('--verbose', help='Outputs verbose status messages', action='store_true', default=True)
args.add_argument('--limit', help='Limit news topics if this parameter provided', type=int, default=2)
args.add_argument('--date', help='Print RSS news from cache', type=int, default=True)
args.add_argument('--to_html', help='Convert RSS news to .html', action='store_true', default=True)
args.add_argument('--to_pdf', help='Convert RSS news to .pdf', action='store_true', default=True)


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = get_config(args.parse_args())


class TestGetConfig(TestConfig):
    def test_json(self):
        self.assertEqual(self.config['json'], True)

    def test_verbose(self):
        self.assertEqual(self.config['verbose'], True)

    def test_limit(self):
        self.assertEqual(self.config['limit'], 2)

    def test_datetime(self):
        self.assertTrue(type(self.config['datetime']), 'str')
