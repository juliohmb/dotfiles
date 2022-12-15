import pyautogui

# Take a screenshot of the selected area
im = pyautogui.screenshot(region=(100, 100, 200, 200))

# Save the screenshot to a file named temp
im.save('temp.png')
