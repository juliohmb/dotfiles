import pyscreenshot as ImageGrab
import pyperclip
import os

def take_screenshot():
    im = ImageGrab.grab()
    im.save("screenshot.png")
    with open("screenshot.png", "rb") as image:
        pyperclip.copy(image.read())

while True:
    if keyboard.is_pressed("ctrl+alt+s"):
        take_screenshot()
        break
