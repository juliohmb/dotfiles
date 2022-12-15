import pyscreenshot as ImageGrab
from PyQt5 import QtWidgets, QtGui, QtCore

class ScreenshotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screenshot")
        self.screenshot_label = QtWidgets.QLabel()
        self.screenshot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.screenshot_label)
        self.setLayout(self.layout)

        # Create a keyboard shortcut for saving the selection to a file
        self.save_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.save_shortcut.activated.connect(self.save_selection)

        # Create a keyboard shortcut for copying the selection to the clipboard
        self.copy_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+C"), self)
        self.copy_shortcut.activated.connect(self.copy_selection)

        # Create a QRubberBand object to allow the user to select an area on the screenshot
        self.selection_band = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self.screenshot_label)
        self.screenshot_label.installEventFilter(self)
        self.selection_start = None
        self.selection_end = None



    def eventFilter(self, obj, event):
        # Handle mouse events on the screenshot_label object to allow the user to select an area
        if obj == self.screenshot_label:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.selection_start = event.pos()
                self.selection_band.setGeometry(QtCore.QRect(self.selection_start, QtCore.QSize()))
                self.selection_band.show()
                return True
            elif event.type() == QtCore.QEvent.MouseMove:
                self.selection_end = event.pos()
                self.selection_band.setGeometry(QtCore.QRect(self.selection_start, self.selection_end).normalized())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.selection_end = event.pos()
                self.selection_band.hide()
                return True
        return super().eventFilter(obj, event)

    def take_screenshot(self):
        self.screenshot = ImageGrab.grab().toqimage()
        self.Q_screenshot = QtGui.QPixmap.fromImage(self.screenshot)
        self.screenshot_label.setPixmap(self.Q_screenshot)

        # Maximize the window
        self.showMaximized()

    def save_selection(self):
        if self.selection_start is not None and self.selection_end is not None:
            # Calculate the coordinates of the selected area
            x1 = min(self.selection_start.x(), self.selection_end.x())
            y1 = min(self.selection_start.y(), self.selection_end.y())
            x2 = max(self.selection_start.x(), self.selection_end.x())
            y2 = max(self.selection_start.y(), self.selection_end.y())
            selected_area = self.screenshot.copy(x1, y1, x2 - x1, y2 - y1)
            selected_area.save("screenshot_selection.png")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ScreenshotWindow()
    window.show()
    app.exec_()
