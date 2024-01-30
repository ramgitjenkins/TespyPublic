from selenium import webdriver

# Set the path to the ChromeDriver executable
chromedriver_path = '/usr/local/bin/chromedriver'

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=chromedriver_path)
 
def test_interaction_with_neo_norwexapac_org(browser):
    # Navigate to the website
    browser.get("https://NEO.norwexapac.org")

    # Perform actions, e.g., inputting text into a search field
    # Assumed there's an input field with id 'input-field'
    input_field = browser.find_element(By.ID, 'ext-comp-1004')
    input_field.send_keys('testadmin') #ID
    input_field = browser.find_element(By.ID, 'ext-comp-1005')
    input_field.send_keys('password') #password

    # Clicking a button
    # Assumed there's a button to click with id 'submit-button'
    submit_button = browser.find_element(By.ID, 'submit-button')
    submit_button.click()

    # Add assertions to verify the results of the actions
    # For example, if you expect to be on a new page, check the URL
    assert "expected_part_of_url" in browser.current_url

    # Or check for text present on the page
    text_element = browser.find_element(By.ID, 'ext-gen17')
    assert "expected text" in text_element.text
