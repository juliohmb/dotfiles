from PIL import ImageGrab
import pyautogui

# Take a screenshot of the entire screen
screenshot = ImageGrab.grab()

# Show the screenshot to the user and let them select an area using the mouse
area = pyautogui.locateOnScreen(screenshot)

# Crop the screenshot to the selected area
cropped_screenshot = screenshot.crop(area)

# Show the cropped screenshot to the user
cropped_screenshot.show()

# Prompt the user to enter a file name for the screenshot
file_name = input("Enter a file name for the screenshot: ")

# Save the screenshot to the specified file
cropped_screenshot.save(file_name)
