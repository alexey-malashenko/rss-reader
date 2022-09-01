"""The module is intended for working with parameters"""

import argparse


def get_args():
    """Define the launcher arguments with the default values.
    Returns:
        launcher parameters
    """

    parser = argparse.ArgumentParser(prog='rss-reader', description="Pure python command-line RSS reader")

    parser.add_argument(
        'source',
        help='RSS URL',
        nargs='?',
        # default='https://news.yahoo.com/rss/'  # TODO: debug
        default='http://rss.cnn.com/rss/edition_world.rss'

    )
    parser.add_argument(
        '--version',
        help='Print version info',
        action='version',
        version='rss_reader 0.0.1'
    )
    parser.add_argument(
        '--json',
        help='Print result as JSON in stdout',
        action='store_true',
        # default=True  # TODO: debug
        default = False  # TODO: debug
    )
    parser.add_argument(
        '--verbose',
        help='Outputs verbose status messages',
        action='store_true',
        default=True  # TODO: debug
        # default = False  # TODO: debug
    )
    parser.add_argument(
        '--limit',
        help='Limit news topics if this parameter provided',
        type=int,
        default=5  # TODO: debug
    )

    return parser.parse_args()
