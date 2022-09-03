import unittest
import sys
from pathlib import Path
from unittest.mock import patch
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.orchestrator import getting_args, getting_config  # noqa: E402


class TestGettingArgs(unittest.TestCase):
    @patch('src.main_reader.orchestrator.getting_args', return_value=True)
    def test_getting_args(self, check_getting_args):
        self.args = getting_args()
        self.assertEqual(str(self.args).rsplit("'")[0], "Namespace(source=")


class TestGettingConfig(unittest.TestCase):
    @patch('src.main_reader.orchestrator.getting_config', return_value=True)
    def test_getting_config(self, check_getting_args):
        self.conf = getting_config()
        self.assertEqual(str(self.conf).rsplit(":")[0], "{'source'")

