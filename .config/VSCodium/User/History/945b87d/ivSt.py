import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QGuiApplication
from PyQt5.QtCore import Qt


class Screenshot(QWidget):
    def __init__(self):
        super().__init__()

        # Create the UI
        self.screenshot_button = QPushButton("Take Screenshot", self)
        self.screenshot_button.clicked.connect(self.take_screenshot)

        self.setGeometry(100, 100, 300, 200)
        self.show()

    def take_screenshot(self):
        # Hide the UI so that it does not appear in the screenshot
        self.hide()

        # Create a QPixmap object to store the screenshot
        screen = QPixmap.grabWindow(QGuiApplication.primaryScreen(), self.x(), self.y(), self.width(), self.height())

        # Save the screenshot to the clipboard
        QGuiApplication.clipboard().setPixmap(screen)

        # Show the UI again
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screenshot = Screenshot()
    sys.exit(app.exec_())
