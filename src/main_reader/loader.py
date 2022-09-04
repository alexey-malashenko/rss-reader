"""The module is intended for loading RSS"""

import feedparser
from .logger import logging_dec, parameter_log
from .checker import check_response


@logging_dec
def loading(url):
    """Define the loading, check the response

        Returns:
              feed dict
        """

    log = parameter_log()
    feed = feedparser.parse(url)  # TODO add try except
    log.info('Got feed: {}'.format(feed))
    if check_response(feed):
        return feed
