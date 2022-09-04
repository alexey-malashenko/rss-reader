"""The module is intended for check response"""

import sys
import json
from logger import logging_dec, parameter_log


@logging_dec
def check_response(resp):
    """Define the response

        Returns:
            True if success
        """

    log = parameter_log()

    if resp['bozo']:
        log.info('Error Response: {}'.format(resp['bozo_exception']))
        sys.exit('Error Response: {}'.format(resp['bozo_exception']))

    else:
        log.info('Response verified')
        return True


def check_cache_file(path):
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
