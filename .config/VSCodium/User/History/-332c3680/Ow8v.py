# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open the file containing the messages
with open('messages.txt', 'r') as file:
    messages = file.readlines()

# Start the webdriver
driver = webdriver.Chrome()

# Go to the WhatsApp web page
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code
input('Press Enter once you have scanned the QR code and select the conversation')

# Get the element containing the input field
input_el = driver.find_element(by=By.CLASS_NAME,value='_3u328')

# Send each message in the file
for message in messages:
    # Clear the input field
    input_el.clear()

    # Enter the message
    input_el.send_keys(message)

    # Wait for the "send" button to appear and click it
    send_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, '_3M-N-'))
    )
    send_button.click()
    time.sleep(2)

# Close the webdriver
driver.quit()
