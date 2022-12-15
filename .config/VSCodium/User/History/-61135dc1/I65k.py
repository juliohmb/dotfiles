import pyscreenshot as ImageGrab
import keyboard

def take_screenshot():
    im = ImageGrab.grab()
    im.save("screenshot.png")

while True:
    if keyboard.is_pressed("ctrl+alt+s"):
        take_screenshot()
        break
