import getpass
import json
import os
from xdg import XDG_CONFIG_HOME

PLAZA_BRIDGE_ENDPOINT_INDEX = "plaza_bridge_endpoint"

global directory, config_file
directory = os.path.join(XDG_CONFIG_HOME, "plaza", "bridges", "gitlab")
config_file = os.path.join(directory, "config.json")


def _get_config():
    if not os.path.exists(config_file):
        return {}
    with open(config_file, "rt") as f:
        return json.load(f)


def _save_config(config):
    os.makedirs(directory, exist_ok=True)
    with open(config_file, "wt") as f:
        return json.dump(config, f)


def get_bridge_endpoint():

    config = _get_config()
    if config.get(PLAZA_BRIDGE_ENDPOINT_INDEX, None) is None:
        config[PLAZA_BRIDGE_ENDPOINT_INDEX] = input("Plaza bridge endpoint: ")
        if not config[PLAZA_BRIDGE_ENDPOINT_INDEX]:
            raise Exception("No bridge endpoint introduced")
        _save_config(config)
    return config[PLAZA_BRIDGE_ENDPOINT_INDEX]