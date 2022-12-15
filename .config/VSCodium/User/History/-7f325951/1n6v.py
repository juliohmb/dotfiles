import pyautogui
import time

# Take a screenshot
screenshot = pyautogui.screenshot()

# Display the screenshot in fullscreen
screenshot.show()

# Wait for the user to select an area
time.sleep(2)

# Get the coordinates of the selected area
selected_area = pyautogui.locateOnScreen('selected_area.png')

# Crop the selected area from the screenshot
cropped_screenshot = screenshot.crop(selected_area)

# Save the cropped screenshot to a file called "temp"
cropped_screenshot.save('temp')
