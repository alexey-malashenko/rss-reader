import sys
from logger import logging_dec, parameter_log


@logging_dec
def check_response(resp):

    log = parameter_log()

    if resp['bozo']:
        log.info('Error Response: {}'.format(resp['bozo_exception']))
        print()
        sys.exit('Error Response: {}'.format(resp['bozo_exception']))

    else:
        log.info('Response verified')
        return True
