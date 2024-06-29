import pyautogui
import time
import random
import os
import json
import logging
import argparse

# Load configuration from file
def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

# Ensure the output directory exists
def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Take a screenshot of the specified region
def take_screenshot(region, output_directory):
    """
    """
    screenshot = pyautogui.screenshot(region = region['x'], region['y'], region['width', region['height'])
                                                                                filename = os.path.join(output_directory, f'screenshot_{int(time.time())}.png')
                                                                                # Save the screenshot with a timestamp
    screenshot.save(filename)
                                                                                logging.info(f'Screenshot saved: {filename}')

                                                                            # Main function to run the screenshot loop
def main(config):
    region = config['region']
    interval_min = config['interval_min']
    interval_max = config['interval_max']
    output_directory = config['output_directory']

    ensure_directory(output_directory)

    logging.info(f'Starting screenshot capture every {interval_min}-{interval_max} seconds...')

    try:
        while True:
            take_screenshot(region, output_directory)
            time.sleep(random.randint(interval_min, interval_max))
    except KeyboardInterrupt:
        logging.info('Screenshot capture stopped by user.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Automate screenshots of a specified screen region.')
    parser.add_argument('--config', type=str, default='config.json', help='Path to the configuration file')

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Load config
    config_path = args.config
    config = load_config(config_path)

    # Run main function
    main(config)
