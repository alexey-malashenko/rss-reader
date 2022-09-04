"""The module is intended for orchestration"""

from .config import get_config
from .args import get_args


def getting_args():
    """Define the getting args

        Returns:
            arguments
        """

    arguments = get_args()
    return arguments


def getting_config():
    """Define the getting config

        Returns:
            config
        """

    arguments = getting_args()
    config = get_config(arguments)
    return config


def get_scenarios(config):
    """Define scenarios:
        1 - get news from URL with limit or without limit
        2 - get news from cache with limit or without limit
        3 - get news from cache and URL with limit or without limit

        Returns:
            config
        """

    if config['source'] and not config['date']:
        config['scenario'] = 'scenario 1: get news from URL with limit or without limit'
    if not config['source'] and config['date']:
        config['scenario'] = 'scenario 2: get news from cache with limit or without limit'
    if config['source'] and config['date']:
        config['scenario'] = 'scenario 3: get news from cache and URL with limit or without limit'
