import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.args import get_args  # noqa: E402


class TestRssCacher(unittest.TestCase):

    def setUp(self):
        self.get_args = get_args()
        self.get_args.source = 'test_args.py'

    def test_get_args(self):
        self.assertEqual(self.get_args.source, 'test_args.py')
        self.assertEqual(self.get_args.json, False)
        self.assertEqual(self.get_args.verbose, False)
        self.assertEqual(self.get_args.limit, False)
        self.assertEqual(self.get_args.date, False)
        self.assertEqual(self.get_args.to_html, False)
        self.assertEqual(self.get_args.to_pdf, False)
