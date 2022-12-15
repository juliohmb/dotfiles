import pyscreenshot as ImageGrab
import os
from pynput import mouse

def take_screenshot():
    print(os.getcwd())
    im = ImageGrab.grab()
    im.save("screenshot.png")

def on_click(x, y, button, pressed):
    if button == mouse.Button.button9 and pressed:
        take_screenshot()

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
