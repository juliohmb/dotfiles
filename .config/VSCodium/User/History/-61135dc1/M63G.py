import pyscreenshot as ImageGrab
import pyperclip
import pyautogui
import keyboard

def take_screenshot():
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im.save("screenshot.png")
    with open("screenshot.png", "rb") as image:
        pyperclip.copy(image.read())

while True:
    if keyboard.is_pressed("ctrl+alt+s"):
        # prompt the user to select the area to capture
        print("Please select the area to capture...")
        x1, y1, x2, y2 = pyautogui.locateOnScreen('select_area.png')
        take_screenshot()
        break