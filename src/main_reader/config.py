"""The module is to get the configuration"""

import datetime


def get_config(args):
    """Define the config

        Returns:
            Config dict
        """

    config = dict()

    config['source'] = args.source

    config['json'] = args.json

    config['verbose'] = args.verbose

    config['limit'] = args.limit

    config['datetime'] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")

    config['date'] = args.date

    config['cache_name'] = 'rss_cache.json'

    config['scenario'] = ''

    return config
