"""The module is to get the configuration"""


def get_config(args):

    config = dict()

    config['source'] = args.source

    config['json'] = args.json

    config['verbose'] = args.verbose

    config['limit'] = args.limit

    return config
