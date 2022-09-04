"""The module is intended for working with parameters"""

import argparse
from src.main_reader import __version__


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
        metavar='source'
    )
    parser.add_argument(
        '--version',
        help='Print version info',
        action='version',
        version='rss_reader ' + __version__
    )
    parser.add_argument(
        '--json',
        help='Print result as JSON in stdout',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '--verbose',
        help='Outputs verbose status messages',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '--limit',
        help='Limit news topics if this parameter provided',
        type=int
    )
    parser.add_argument(
        '--date',
        help='Print RSS news from cache',
        action='store_true'
    )

    return parser.parse_args()
