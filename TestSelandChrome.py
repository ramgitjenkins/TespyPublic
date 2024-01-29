from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Navigate to a website (change the URL to your desired website)
url = 'https://www.example.com'
driver.get(url)

# Verify the page title
expected_title = 'Example Domain'
actual_title = driver.title

# Output the test result
if expected_title in actual_title:
    print(f'Test Passed! Page title is: {actual_title}')
else:
    print(f'Test Failed! Expected title: {expected_title}, Actual title: {actual_title}')

# Close the browser
driver.quit()
