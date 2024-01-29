import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def test_example_domain():
    # Firefox options (similar to Chrome options)
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Runs Firefox in headless mode.

    # Set the path to the GeckoDriver executable
    geckodriver_path = '/usr/local/bin/geckodriver'

    # Initialize the Firefox WebDriver with options
    s = Service(geckodriver_path)
    driver = webdriver.Firefox(service=s, options=firefox_options)

    try:
        # Navigate to a website (change the URL to your desired website)
        url = 'https://www.example.com'
        driver.get(url)

        # Verify the page title
        expected_title = 'Example Domain'
        actual_title = driver.title

        assert expected_title in actual_title, f"Test Failed! Expected title: {expected_title}, Actual title: {actual_title}"
        print(f'Test Passed! Page title is: {actual_title}')

    finally:
        # Close the browser
        driver.quit()
