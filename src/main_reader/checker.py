"""The module is intended for check response"""

import sys
import json
from .logger import logging_dec, parameter_log


log = parameter_log()


@logging_dec
def check_response(resp):
    """Define the response

        Returns:
            True if success
        """

    if resp['bozo']:
        log.info('Error Response: {}'.format(resp['bozo_exception']))
        sys.exit('Error Response: {}'.format(resp['bozo_exception']))

    else:
        log.info('Response verified')
        return True


@logging_dec
def check_cache_file(path):
    """Define the checking for cache

        Returns:

        """

    try:
        with open(path, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        with open(path, 'w', encoding='utf-8') as f:
            template = {"00000001_www.test-source_a": {"publish_date": '00000001', "Feed": "feed_a", "Title": "title",
                                                       "Date": "date", "Link": "link", "Links": "links",
                                                       "Source": "a"}}

            json_template = json.dumps(template, sort_keys=True)
            f.write(json_template)
        log.info('Writing to json_template successful {}'.format(''))


@logging_dec
def check_full_rss_lst(*args):
    """Define the checking for full rss list

        Returns:
            full_lst if exist
        """

    full_lst = []

    if args:
        for arg in args:
            for news in arg:
                for key, value in news.items():
                    full_lst.append(value)

        log.info('Got list: {}'.format(full_lst))
        return full_lst

    else:
        print('no news')

    return False
