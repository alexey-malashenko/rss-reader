"""The module is intended for orchestration"""

from config import get_config
from args import get_args


def getting_args():
    """Define the getting args

        Returns:
            arguments
        """

    arguments = get_args()
    return arguments


def getting_config():
    """Define the getting config

        Returns:
            config
        """

    arguments = getting_args()
    config = get_config(arguments)
    return config
