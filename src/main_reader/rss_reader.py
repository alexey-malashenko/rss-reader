"""The module is a core"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[1].joinpath('src')))
sys.path.append(str(Path(__file__).parents[1].joinpath('src', 'main_reader')))
from src.main_reader.logger import logging_dec, parameter_log  # noqa: E402
from src.main_reader.orchestrator import getting_args, getting_config, get_scenarios  # noqa: E402
from src.main_reader.loader import loading  # noqa: E402
from src.main_reader.rss_parser import Rss  # noqa: E402
from src.main_reader.cache_reader import RssCacher  # noqa: E402
from src.main_reader.converter import converter  # noqa: E402
from src.main_reader.checker import check_full_rss_lst  # noqa: E402

log = parameter_log()
args = getting_args()
config = getting_config()
get_scenarios(config)

sys.path.append(str(Path(__file__).parents[1].joinpath('main_reader', 'cache')))
path_cache = str(Path(__file__).parents[1].joinpath('main_reader', 'cache', config['cache_name']))
path_html_tmpl = str(Path(__file__).parents[1].joinpath('main_reader', 'template'))
path_html_out = str(Path(__file__).parents[1].joinpath('main_reader', 'output', config['path_for_html']))
path_pdf_out = str(Path(__file__).parents[1].joinpath('main_reader', 'output', config['path_for_pdf']))


log.info('Started with args: {}'.format(args))
log.info('Started with configuration: {}'.format(config))


@logging_dec
def main():
    """The entry point for RSS reader

    Returns:
        None
    """
    full_lst = []

    if config['scenario'] == 'scenario 1: get news from URL with limit or without limit':
        response = loading(config['source'])
        rss = Rss(response, config, path_cache)
        rss.print_rss()
        full_lst = check_full_rss_lst(rss.cash)

    if config['scenario'] == 'scenario 2: get news from cache with limit or without limit':
        rss_cache = RssCacher(config, path_cache)
        rss_cache.print_rss()
        full_lst = check_full_rss_lst(rss_cache.cache_limited)

    if config['scenario'] == 'scenario 3: get news from cache and URL with limit or without limit':
        rss_cache = RssCacher(config, path_cache)
        rss_cache.print_rss()
        response = loading(config['source'])
        rss = Rss(response, config, path_cache)
        rss.print_rss()
        full_lst = check_full_rss_lst(rss.cash, rss_cache.cache_limited)

    converter(config, full_lst, path_html_tmpl, path_html_out, path_pdf_out)


if __name__ == "__main__":
    main()
