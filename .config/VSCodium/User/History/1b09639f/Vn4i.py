import datetime
import pyautogui
from PIL import Image

# Take a screenshot and save it as a PIL image object
screenshot = pyautogui.screenshot()

# Allow the user to select an area of the screenshot
area = pyautogui.get_image_region_of_interest(screenshot)

# Display the selected area in a borderless, fullscreen window
area.show(title=None, fullscreen=True)

# Check if the user pressed Ctrl+S or Ctrl+C
if pyautogui.keyDown("ctrl") and pyautogui.keyDown("s"):
    # If Ctrl+S is pressed, save the image to a file with the current date
    date_string = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"screenshot-{date_string}.png"
    area.save(filename)
elif pyautogui.keyDown("ctrl") and pyautogui.keyDown("c"):
    # If Ctrl+C is pressed, save the image to the clipboard
    pyautogui.copyImage(area)

# Close the window displaying the selected area
pyautogui.get_windows_with_title(None)[0].close()
