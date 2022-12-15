import pyautogui

# Prompt the user to select an area of the screen
print('Please select the area of the screen that you want to screenshot.')
im = pyautogui.screenshot('temp.png', region=pyautogui.locateOnScreen('selector.png'))

# Save the screenshot to a file named temp
im.save('temp.png')
