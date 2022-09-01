"""The module is to get the configuration"""
import datetime


def get_config(args):

    config = dict()

    config['source'] = args.source

    config['json'] = args.json

    config['verbose'] = args.verbose

    config['limit'] = args.limit

    config['datetime'] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")

    return config
