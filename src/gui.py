"""
Module: gui

Contains the ScreenshotApp class for the GUI application.
"""

from tkinter import Tk, Label, Button, Entry, StringVar, filedialog
import threading
import logging
from .config_loader import load_config
from .screenshot_taker import take_screenshot, ensure_directory
from .archiver import archive_old_screenshots

class ScreenshotApp:
    """
    A GUI application for automating screenshots.
    """
    def __init__(self, master):
        """
        Initialize the ScreenshotApp with a master Tkinter instance.
        """
        self.master = master
        master.title("Screenshot Automation")

        self.config_path = StringVar(value = '../config/config.json')

        self.label = Label(master, text = "configuration File:")
        self.label.pack()

        self.entry = Entry(master, textvariable = self.config_path)
        self.entry.pack()

        self.browse_button = Button(
                master, text = "Browse", command = self.browse_file)
        self.browse_button.pack()

        self.start_button = Button(master, text = "Start", command = self.start)
        self.start_button.pack()

        self.stop_button = Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.running = False

        def browse_file(self):
            """
            Open a file dialog to select a configuration file.
            """
            filename = filedialog.askopenfilename()
            self.config_path.set(filename)

        def start(self):
            """
            Start the screenshot automation process.
            """
            self.running = True
            thread = threading.Thread(target = self.run_screenshot_loop)
            thread.start()

        def stop(self):
            """
            Stop the screenshot automation process.
            """
            self.running = False

        def run_screenshot_loop(self):
            """
            Run the screenshot loop, taking screenshots at random intervals.
            """
            config = load_config(self.config_path.get())
            region = config['region']
            interval_min = config['interval_min']
            interval_max = config['interval_max']
            output_directory = config['output_directory']
            archive_days = config.get('archive_days', 7)

            ensure_directory(output_directory)

            log_msg = "'Starting screenshot capture every"
            logging.info(f'{log_msg } {interval_min}-{interval_max} seconds...')

            try:
                while self.running:
                    take_screenshot(region, output_directory)
                    archive_old_screenshots(output_directory, archive_days)
                    self.master.update()
                    time.sleep(random.randint(interval_min, interval_max))
            except Exception as e:
                logging.error(f'An error occurred: {e}')
                self.running = False

