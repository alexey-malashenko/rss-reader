import unittest
import sys
from pathlib import Path
from unittest.mock import patch
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.loader import loading  # noqa: E402


class TestLoading(unittest.TestCase):
    @patch('src.main_reader.loader.check_response', return_value=True)
    def test_loading(self, check_response):
        self.loading = loading('http://localhost:8000')
        self.assertEqual(self.loading['bozo'], True)



