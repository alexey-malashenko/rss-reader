"""The module is a core"""

from logger import logging_dec, parameter_log
from orchestrator import getting_args, getting_config
from loader import loading
from rss_parser import Rss


log = parameter_log()
args = getting_args()
config = getting_config()


log.info('Started with args: {}'.format(args))
log.info('Started with configuration: {}'.format(config))


@logging_dec
def main():
    """The entry point for RSS reader

    Returns:
        None
    """

    response = loading(config['source'])
    print(type(response))
    rss = Rss(response, config)
    rss.print_rss()


if __name__ == "__main__":
    main()
