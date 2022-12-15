import pyscreenshot as ImageGrab
import pyperclip
import os
from pynput import keyboard

def take_screenshot():
    im = ImageGrab.grab()
    im.save("screenshot.png")
    with open("screenshot.png", "rb") as image:
        pyperclip.copy(image.read())

def on_press(key):
    if key == keyboard.Key.ctrl_l and key == keyboard.Key.alt_l and key == keyboard.Key.s:
        take_screenshot()

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
