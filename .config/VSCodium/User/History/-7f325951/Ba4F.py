import os
import time
import pyautogui

# Take a screenshot and save it to a temporary file.
screenshot = pyautogui.screenshot()
screenshot.save('temp.png')

# Display the screenshot in fullscreen mode.
screenshot.show()

# Allow the user to select an area on the screen with the mouse.
# This will return a tuple with the coordinates of the selected area.
area = pyautogui.locateOnScreen('temp.png')

# Save the selected area to a file named "temp".
screenshot.crop(area).save('temp.png')
