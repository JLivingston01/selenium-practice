from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver (adjust the path as necessary)
driver = webdriver.Chrome()

try:
    # Open the website
    driver.get("https://thedataprofessional.com")  # Replace with your target URL
    time.sleep(2)  # Wait for the page to load

    # Click the "About" link
    about_link = driver.find_element(By.LINK_TEXT, "ABOUT")
    about_link.click()
    time.sleep(2)  # Wait to observe the result
finally:
    # Close the browser
    driver.quit()