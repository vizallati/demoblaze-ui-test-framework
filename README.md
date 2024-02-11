# Table of Contents

1. [Demoblaze UI Test Framework](#demoblaze-ui-test-framework)
   1. [Features](#features)
   2. [Getting Started](#getting-started)
      1. [Prerequisites](#prerequisites)
      2. [Clone Repository](#clone-repository)
      3. [Installation](#installation)
      4. [Running Tests](#running-tests)
      5. [Generating Allure Report](#generating-allure-report)
      6. [Issues found](#issues-found)
      
# Demoblaze UI Test Framework

This repository contains an automation framework built using Python and Selenium for testing the Demoblaze Product Store website as part of Ito World's QA UI technical test exercise. This framework incorporates the use of Behavior-Driven Development (BDD) principles using Gherkin syntax and Allure reporting for comprehensive test result analysis.

## Features

Selenium Integration: Utilize the Selenium automation tool for smooth browser automation across various web browsers

BDD Testing: Adopt Behavior-Driven Development by expressing test scenarios in Gherkin syntax. Write clear and concise feature files in the features directory.

Allure Reporting: Generate detailed and visually appealing test reports with Allure, providing insights into test execution, failures, and trends.

## Getting Started
### Prerequisites
Before you begin, ensure you have met the following requirements:

[Python 3.11](https://www.python.org/downloads/release/python-3110/) or higher

Allure (installation instructions [here](https://allurereport.org/docs/gettingstarted-installation/))
### Clone Repository
To clone the repository, run the following command in your terminal:


```bash
git clone https://github.com/vizallati/demoblaze-ui-test-framework.git
```
### Installation

1. Navigate to the project directory 
```bash
cd demoblaze-ui-test-framework
```
2. Create virtual environment
```bash
python -m venv virtual_environment
```
3. Activate virtual environment
```bash
# On Windows
virtual_environment\Scripts\activate
# On macOS/Linux
source virtual_environment/bin/activate
```
4. Install the required dependencies:

```bash
pip install -r requirements.txt
```
### Running Tests
Before running the tests edit the settings.yml file with respective values and make sure you have the browser specified in the pytest.ini file installed (Google Chrome or Microsoft Edge)

Run the tests using the following command:

```bash
pytest
```
This command will execute the tests and generate Allure report data in the allure-results directory (These run configurations like browser option are all set in the pytest.ini file)

### Generating Allure Report
To generate and view the Allure report, run the following commands:

```bash
allure serve path-to-allure-results
```
This will generate the Allure report and open it in your default web browser.

### Issues found
1. User is able to place order with no item present in cart
2. User is able to send contact message without filling any of the fields in the contact form.
3. User is able to place order after filling only name and credit card number
4. The place order form does not ask for contact information (email or phone number) needed to update the customer on the progress of their order, and credit card CVV
