"""
Module: config_loader

Contains functions for loading configuration files.
"""

import json

def load_config(config_path):
    """
    Load the JSON configuration file from the given path.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        dict: Parsed configuration data.
    """
    with open(config_path, 'r') as f:
        return json.load(f)
