import logging
from orchestrator import getting_args


def parameter_log():

    args = getting_args()

    if args.verbose:
        logging.disabled = False
        logging.basicConfig(
            format='%(asctime)s [%(levelname)s] %(message)s ',
            datefmt='%d-%b-%y %H:%M:%S',
            level=logging.INFO
        )
    else:
        logging.disabled = True
    return logging


def logging_dec(func):

    log = parameter_log()

    def wrapper(*args, **kwargs):
        log.info('Started func: {}'.format(func.__name__))
        result = func(*args, **kwargs)
        log.info('Conpleted func: {}'.format(func.__name__))

        return result

    return wrapper
