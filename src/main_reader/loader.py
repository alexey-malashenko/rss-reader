import feedparser
from logger import logging_dec, parameter_log
from checker import check_response
from exceptions import NoDataToConvertError


@logging_dec
def loading(url):
    log = parameter_log()
    feed = feedparser.parse(url)  # TODO add try except
    log.info('Got feed: {}'.format(feed))
    if check_response(feed):
        return feed
