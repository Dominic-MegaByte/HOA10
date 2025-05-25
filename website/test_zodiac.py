from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH or provide full path

# URL where the search form is hosted
driver.get("http://127.0.0.1:8000/signs/")

# Wait for the page to load
time.sleep(2)

# Locate the search input field and enter a search term
search_box = driver.find_element(By.NAME, "searched")
search_box.send_keys("Aries")  # Replace with a zodiac sign you expect to match

# Submit the form (by hitting Enter or clicking the button)
search_box.send_keys(Keys.RETURN)

# Wait for the results to load
time.sleep(3)

# Check if results appear
try:
    results_header = driver.find_element(By.XPATH, "//h2[contains(text(),'Search Results')]")
    print("Search results found:", results_header.text)

    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    print(f"Number of result rows (including headers): {len(rows)}")
except Exception as e:
    print("No results found or error occurred:", e)

# Close the browser
driver.quit()
