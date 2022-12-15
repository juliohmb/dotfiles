import pyscreenshot as ImageGrab
import os
from pynput import mouse

def take_screenshot():
    print(os.getcwd())
    im = ImageGrab.grab()
    im.save("screenshot.png")

def on_click(x, y, button, pressed):
    print(f"Mouse button used: {button}")
    if button == mouse.Button.right and pressed:
        take_screenshot()

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
