"""
Module: main

The entry point for the screenshot automation application.
"""

import logging
from tkinter import Tk
from .gui import ScreenshotApp

if __name__ == "__main__":
    # Set up logging
    log_filename = f'../logs/screenshot_automation_{int(time.time())}.log'
    logging.basicConfig(
            level=logging.INFO, format='%(asctime)s - %(levelname)s - %(
            message)s', filename=log_filename, filemode='w')

    # Create the GUI
    root = Tk()
    app = ScreenshotApp(root)
    root.mainloop()
