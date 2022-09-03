import unittest
import sys
from pathlib import Path
from unittest.mock import patch
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.checker import check_response  # noqa: E402

resp = {'test': True, 'bozo': False}


class TestChecker(unittest.TestCase):
    def setUp(self):
        self.resp = check_response(resp)


class TestGetConfig(TestChecker):
    def test_resp(self):
        self.assertEqual(self.resp, True)
