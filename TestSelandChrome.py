from selenium import webdriver

# Replace with the path to your ChromeDriver executable
chromedriver_path = '/usr/local/bin/chromedriver'

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Open a website (e.g., Google)
driver.get("https://www.google.com")

# Verify the page title
if "Google" in driver.title:
    print("Google is open!")
else:
    print("Google is not open!")

# Close the WebDriver
driver.quit()
