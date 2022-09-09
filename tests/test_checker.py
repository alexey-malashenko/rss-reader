import unittest
import pytest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.checker import check_response, check_full_rss_lst  # noqa: E402

resp = {'test': True, 'bozo': False}


class TestChecker(unittest.TestCase):
    def setUp(self):
        self.resp = check_response(resp)
        self.check_full_rss_lst = check_full_rss_lst


class TestGetConfig(TestChecker):
    def test_resp(self):
        self.assertEqual(self.resp, True)

    def test_resp_exit(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            resp_true = {'test': True, 'bozo': True, 'bozo_exception': 'Invalid URL'}
            check_response(resp_true).will_exit_somewhere_down_the_stack()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 'Error Response: Invalid URL'


class TestCheckResponse(TestChecker):
    def test_full_rss_lst(self):
        resp_true = [{'test': True, 'bozo': True, 'bozo_exception': 'Invalid URL'}, ]
        self.assertEqual(self.check_full_rss_lst(resp_true), [True, True, 'Invalid URL'])
