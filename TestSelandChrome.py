import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def browser():
    # Firefox options (similar to Chrome options)
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Runs Firefox in headless mode.

    # Set the path to the GeckoDriver executable
    geckodriver_path = '/usr/local/bin/geckodriver'

    # Initialize the Firefox WebDriver with options
    s = Service(geckodriver_path)
    driver = webdriver.Firefox(service=s, options=firefox_options)
    driver.implicitly_wait(10)  # waits for the element to be present, up to 10 seconds
    yield driver
    driver.quit()

def test_interaction_with_neo_norwexapac_org(browser):
    # Navigate to the website
    browser.get("https://NEO.norwexapac.org")

    # Perform actions, e.g., inputting text into a search field
    # Assumed there's an input field with id 'input-field'
    input_field = browser.find_element(By.ID, 'ext-comp-1004')
    input_field.send_keys('testadmin')  # username
    input_field = browser.find_element(By.ID, 'ext-comp-1005')
    input_field.send_keys('password')  # password

    # Clicking a button
    # Assumed there's a button to click with id 'submit-button'
    submit_button = browser.find_element(By.ID, 'ext-gen17')
    submit_button.click()

    # Add assertions to verify the results of the actions
    # For example, if you expect to be on a new page, check the URL
    assert "expected_part_of_url" in browser.current_url

    # Or check for text present on the page
    text_element = browser.find_element(By.ID, 'ext-gen17')
    assert "expected text" in text_element.text
