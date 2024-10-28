from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
USER_DATA_DIR = os.getenv("USER_DATA_DIR")  # Path to saved browser session
AZURE_BOARD_URL = os.getenv("AZURE_BOARD_URL")  # Azure board URL
WHATSAPP_PHONE = os.getenv("WHATSAPP_PHONE")  # WhatsApp phone number

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
old_products = 0

while True:
    driver.get(AZURE_BOARD_URL)
    new_products = driver.find_elements(By.CSS_SELECTOR,
                                        'div[class="cell member-content member content proposed ui-droppable"] div[class="id"]')
    print('New products =', len(new_products))

    if old_products < len(new_products):
        old_products = len(new_products)
        driver.implicitly_wait(5)
        driver.get(f'https://wa.me/{WHATSAPP_PHONE}')
        driver.implicitly_wait(10)

        # Continue to chat button
        driver.find_element(By.ID, 'action-button').click()

        # WhatsApp Web
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//span[contains(text(),'use WhatsApp Web')]").click()

        time.sleep(20)
        # Type message and send
        message_box = driver.find_element(By.XPATH, '(//p[@class="selectable-text copyable-text iq0m558w"])[2]')
        message_box.send_keys("Reminder! New tickets are here!!!!", Keys.ENTER)

        print("Messaged")
    
    print('Sleeping for 10 minutes')
    time.sleep(600)
    print("Checking again!")
