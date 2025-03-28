## The test cases have been automated using Playwright and Pytest. 
## Below are the instructions on how to install the required libraries and run tests.

### Installation instructions
1. Download the latest Python version from https://www.python.org/downloads and install it (if not installed).
2. Download the latest version of Git from https://git-scm.com/downloads and install it (if not installed).
3. Install the Pytest plugin using pip install "pytest-playwright".
4. Install the Pytest browsers with "playwright install".

### Repository setup
1. Clone the Repositoryfrom https://github.com/ivanvalchuk/ui-automation-task.git
2. "cd" to the folder "ui-automation-task" and go to "tests".
3. Run the following commands for launching tests:
    - "./tests/test_desktop.py" contains test cases for running on Desktop.
    - "./tests/test_mobile.py" contains test cases for running on Mobile.

### Running intstructions
- "pytest -m desktop" - runs the tests on Desktop browsers (e.g. Chromium)
- "pytest -m mobile" - runs the tests on emualated mobile devices (e.g. iPhone 15)
- "pytest -m desktop --lf" / "pytest -m mobile --lf" - re-runs the previous failed tests for Desktop / Mobile

### How to set up reporting
1. Install the plugin for Alure reporting using "pip install allure-pytest".
2. Install Allure via "brew install allure" for Mac or check https://allurereport.org/docs/install for other operating systems.
3. "cd" to the folder "ui-automation-task" and go to "tests".
4. Run the command for generating the report: "allure serve report".
