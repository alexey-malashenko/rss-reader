import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.rss_reader import main  # noqa: E402


class TestRss(unittest.TestCase):
    def test_main(self):
        self.main = main
        self.assertEqual(str(type(self.main)), "<class 'function'>")
