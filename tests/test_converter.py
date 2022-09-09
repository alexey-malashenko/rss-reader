import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.converter import converter, convert_to_html, save_to  # noqa: E402

resp = {'test': True, 'bozo': False}


class TestChecker(unittest.TestCase):
    def setUp(self):
        self.converter = converter
        self.convert_to_html = convert_to_html
        self.save_to = save_to


class TestGetConfig(TestChecker):
    def test_converter(self):
        self.assertEqual(self.converter(1, [], 'test', 'test', 'test'), None)

    def test_convert_to_html(self):
        path_html_tmpl = str(Path(__file__).parents[1].joinpath('src', 'main_reader', 'template'))
        self.assertEqual(self.convert_to_html([], path_html_tmpl), None)

    def test_save_to_html(self):
        config = {'to_html': True, 'to_pdf': False}
        html_rss = ''
        path_html_out = str(Path(__file__).parents[1].joinpath('src', 'main_reader', 'output', 'test.html'))
        path_pdf_out = str(Path(__file__).parents[1].joinpath('src', 'main_reader', 'output', 'test.pdf'))
        self.assertEqual(self.save_to(config, html_rss, path_html_out, path_pdf_out), None)

    def test_save_to_pdf(self):
        config = {'to_html': False, 'to_pdf': True}
        html_rss = ''
        path_html_out = str(Path(__file__).parents[1].joinpath('src', 'main_reader', 'output', 'test.html'))
        path_pdf_out = str(Path(__file__).parents[1].joinpath('src', 'main_reader', 'output', 'test.pdf'))
        self.assertEqual(self.save_to(config, html_rss, path_html_out, path_pdf_out), None)
