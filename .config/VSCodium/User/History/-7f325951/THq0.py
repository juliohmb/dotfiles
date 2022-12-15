import pyautogui

# prompt the user to select the area for the screenshot
print("Please select the area for the screenshot by dragging your mouse.")

# take the screenshot of the selected area
screenshot = pyautogui.screenshot(region=pyautogui.get_display_size())

# save the screenshot
screenshot.save("screenshot.png")
