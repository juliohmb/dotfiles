import datetime
import pyautogui
from PIL import Image

# Take a screenshot and save it as a PIL image object
screenshot = pyautogui.screenshot()

# Allow the user to select an area of the screenshot
area = pyautogui.locateOnScreen(screenshot)

# Display the selected area in a borderless, fullscreen window
area.show(title=None, fullscreen=True)

# Check if the user pressed Ctrl+S or Ctrl+C
if pyautogui.keyDown("ctrl") and pyautogui.keyDown("s"):
    # If Ctrl+S is pressed, save the image to a file with the current date
    date_string = datetime.datetime.now().strftime
