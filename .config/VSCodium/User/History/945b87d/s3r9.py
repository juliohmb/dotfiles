import pyscreenshot as ImageGrab
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import Qt

# Take a screenshot and store it in a QPixmap object
screenshot = ImageGrab.grab()

# Save the screenshot to the clipboard
app = QGuiApplication()
app.clipboard().setPixmap(screenshot)
