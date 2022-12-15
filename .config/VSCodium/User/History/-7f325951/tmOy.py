from PIL import ImageGrab
import pyautogui

# Take a screenshot of the entire screen
screenshot = ImageGrab.grab()

# Show the screenshot to the user and let them select an area using the mouse
area = pyautogui.locateOnScreen(screenshot)

# Save the selected area to a file called "temp"
screenshot.crop(area).save("temp.png")
