import pyscreenshot as ImageGrab
from PyQt5 import QtWidgets, QtGui

class ScreenshotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screenshot")
        self.screenshot_label = QtWidgets.QLabel()
        self.screenshot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshot_button = QtWidgets.QPushButton("Take Screenshot")
        self.screenshot_button.clicked.connect(self.take_screenshot)
        self.save_button = QtWidgets.QPushButton("Save Selection")
        self.save_button.clicked.connect(self.save_selection)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.screenshot_label)
        self.layout.addWidget(self.screenshot_button)
        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

    def take_screenshot(self):
        self.screenshot = ImageGrab.grab()
        self.screenshot_label.setPixmap(QtGui.QPixmap.fromImage(self.screenshot))

    def save_selection(self):
        selected_area = self.screenshot_label.pixmap().copy(self.screenshot_label.selection_area)
        selected_area.save("screenshot_selection.png")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ScreenshotWindow()
    window.show()
    app.exec_()
