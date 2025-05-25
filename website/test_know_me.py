from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the webpage (Update this URL to match your local Django server)
    driver.get("http://127.0.0.1:8000/know/")  

    # Find all interactive cards
    cards = driver.find_elements(By.CLASS_NAME, "card-hoa5")

    for card in cards:
        # Get the initial text of the card
        initial_text = card.text
        print(f"Before click: {initial_text}")

        # Click the card
        card.click()
        time.sleep(1)  # Allow time for animation

        # Check if image is added (the card content should change)
        new_content = card.get_attribute("innerHTML")
        if "<img" in new_content:
            print(f"PASS: Card '{initial_text}' changed to an image")
        else:
            print(f"FAIL: Card '{initial_text}' did not change")

        # Click again to revert
        card.click()
        time.sleep(1)

        # Verify it returns to the original text
        if card.text == initial_text:
            print(f"PASS: Card '{initial_text}' reverted back")
        else:
            print(f"FAIL: Card '{initial_text}' did not revert")

finally:
    # Close browser after test
    time.sleep(2)
    driver.quit()
