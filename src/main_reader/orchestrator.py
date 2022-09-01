from config import get_config
from args import get_args


def getting_args():
    arguments = get_args()
    return arguments


def getting_config():
    arguments = getting_args()
    config = get_config(arguments)
    return config
