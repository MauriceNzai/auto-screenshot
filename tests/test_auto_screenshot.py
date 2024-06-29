import unittest
import os
from src.config_loader import load_config
from src.screenshot_taker import take_screenshot, ensure_directory
from src.archiver.py import archive_old_screenshots

class TestScreenshotAutomation(unittest.TestCase):

    def setUp(self):
        self.config = load_config('config/config.json')
        self.output_directory = self.config['output_directory']

    def test_ensure_directory(self):
        ensure_directory(self.output_directory)
        self.assertTrue(os.path.exists(self.output_directory))

    def test_take_screenshot(self):
        ensure_directory(self.output_directory)
        initial_files = len(os.listdir(self.output_directory))
        take_screenshot(self.config['region'], self.output_directory)
        final_files = len(os.listdir(self.output_directory))
        self.assertEqual(final_files, initial_files + 1)

    def test_archive_old_screenshots(self):
        # Archive tests would require creating old files and checking if they get moved.
        # This is a simplified test example.
        ensure_directory(self.output_directory)
        archive_old_screenshots(self.output_directory, 0)  # Archive all files for testing
        archive_dir = os.path.join(self.output_directory, "archive")
        self.assertTrue(os.path.exists(archive_dir))
        self.assertGreater(len(os.listdir(archive_dir)), 0)

if __name__ == '__main__':
    unittest.main()
