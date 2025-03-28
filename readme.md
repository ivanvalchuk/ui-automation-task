The test cases have been automated using Playwright and Pytest. Below are the instructions on how to install the required libraries and run tests.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Installation instructions:
Download the latest Python version from https://www.python.org/downloads and install it.
Download the latest version of Git from https://git-scm.com/downloads and install it.
Install the Pytest plugin using pip install "pytest-playwright".
Install the required browsers with "playwright install".
Clone repository from https://github.com/ivanvalchuk/ui-automation-task.git
"cd" to the folder "ui-automation-task" and go to "tests".
 - "./tests/test_desktop.py" contains test cases for running on Desktop.
 - "./tests/test_mobile.py" contains test cases for running on Mobile.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Running intstructions"
"pytest -m desktop" - runs the tests on Desktop browsers (e.g. Chromium)
"pytest -m mobile" - runs the tests on emualated mobile devices (e.g. iPhone 15)
"pytest -m desktop --lf" / "pytest -m mobile --lf" - re-runs the previous failed tests for Desktop / Mobile
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
How to set up reporting"
Install the plugin for Alure reporting using "pip install allure-pytest"
Install Allure via "brew install allure" on Mac or check https://allurereport.org/docs/install for other operating systems.
"cd" to the folder "ui-automation-task" and go to "tests".
Run the command for generating the report: "allure serve report".
