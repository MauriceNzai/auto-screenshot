"""
Module: archiver

Contains functions for archiving old screenshots.
"""

import os
import time
import shutil
import logging

def archive_old_screenshots(output_directory, archive_days):
    """
    Archive screenshots older than a specified number of days.

    Args:
        output_directory (str): Directory containing the screenshots.
        archive_days (int): Number of days after which screenshots should be archived.
    """
    now = time.time()
    cutoff = now - (archive_days * 86400)
    archive_directory = os.path.join(output_directory, "archive")
    if not os.path.exists(archive_directory):
        os.makedirs(archive_directory)

    for filename in os.listdir(output_directory):
        filepath = os.path.join(output_directory, filename)
        is os.path.isfile(filepath):
            file_modified = os.path.getmtime(filepath)
            if file_modified < cutoff:
                shutil.move(filepath, os.path.join(
                    archive_directory, filename))
                logging.infor(f'Archived screenshot: {filename}')
