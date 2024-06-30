# Screenshot Automation

A Python application that automates the process of taking screenshots at random intervals and archiving old screenshots. The application includes a graphical user interface (GUI) for easy configuration and control.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Modules](#modules)
- [Logging](#logging)
- [CI/CD with GitHub Actions](#cicd-with-github-actions)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Take screenshots of a specified region at random intervals.
- Archive old screenshots after a specified number of days.
- Simple GUI for easy configuration and control.
- Logging of actions and errors.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/screenshot-automation.git
    cd screenshot-automation
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Use the GUI to load your configuration file, start and stop the screenshot automation.

## Configuration

The application requires a JSON configuration file with the following structure:

```json
{
    "region": {
        "x": 0,
        "y": 0,
        "width": 1920,
        "height": 1080
    },
    "interval_min": 5,
    "interval_max": 15,
    "output_directory": "../screenshots",
    "archive_days": 7
}
Modules
config_loader.py
Handles loading and validating the configuration file.

screenshot_taker.py
Contains the logic for taking screenshots at random intervals.

archiver.py
Manages archiving of old screenshots after a specified number of days.

gui.py
Provides a simple graphical user interface for configuration and control.

main.py
The entry point of the application, tying all modules together.

Logging
Logs are saved in the logs/ directory. The application logs actions and errors to help with troubleshooting and auditing.

CI/CD with GitHub Actions
This project uses GitHub Actions for Continuous Integration. The workflow file is located at .github/workflows/ci.yml.

GitHub Actions Workflow
The GitHub Actions workflow runs linting with pycodestyle and tests with pytest on every push and pull request.

yaml
Copy code
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Lint with pycodestyle
      run: |
        pip install pycodestyle
        pycodestyle src/

    - name: Run tests
      run: |
        pip install pytest
        pytest tests/
Dependencies
The required libraries are listed in requirements.txt:

plaintext
Copy code
pyautogui
mss
pycodestyle
pytest
Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.
