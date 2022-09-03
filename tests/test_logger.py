import unittest
import sys
from pathlib import Path
from unittest.mock import patch
import logging
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.logger import parameter_log, logging_dec  # noqa: E402


class TestParameterLog(unittest.TestCase):
    @patch('src.main_reader.logger.parameter_log', return_value=logging)
    def test_parameter_log(self, check_response):
        self.log = parameter_log()
        self.assertEqual(self.log, logging)


class TestLoggingDec(unittest.TestCase):
    @patch('src.main_reader.logger.logging_dec', return_value=logging)
    def test_logging_dec(self, check_response):
        self.log = parameter_log()
        self.assertEqual(self.log, logging)

