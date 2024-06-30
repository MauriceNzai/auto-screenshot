"""
Module: screenshot_taker

Contains functions for taking screenshots and ensuring directories exist.
"""

import pyautogui
import time
import os
import logging


def ensure_directory(directory):
    """
    Ensure the specified directory exists, creating it if necessary.

    Args:
        directory (str): Path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def take_screenshot(region, output_directory):
    """
    Take screenshot of specified region and save it to output directory.

    Args:
        region (dict): A dictionary containing the 'x', 'y', 'width',
        and 'height' of the region.
        output_directory (str): Directory to save the screenshot.
    """
    screenshot = pyautogui.screenshot(region=(
        region['x'], region['y'], region['width'], region['height']))
    filename = os.path.join(
            output_directory, f'screenshot_{int(time.time())}.png')
    screenshot.save(filename)
    logging.info(f'Screenshot saved: {filename}')
