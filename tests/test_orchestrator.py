import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.orchestrator import getting_args, getting_config  # noqa: E402


class TestGettingArgs(unittest.TestCase):
    def test_getting_args(self):
        self.args = getting_args()
        self.assertEqual(str(self.args).rsplit("'")[0][:17], "Namespace(source=")


class TestGettingConfig(unittest.TestCase):
    def test_getting_config(self):
        self.conf = getting_config()
        self.assertEqual(str(self.conf).rsplit(":")[0], "{'source'")
