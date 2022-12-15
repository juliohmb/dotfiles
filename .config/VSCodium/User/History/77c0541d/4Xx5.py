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

        # Take a screenshot when the program starts
        self.take_screenshot()

        # Create a keyboard shortcut for saving the selection
        self.save_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.save_shortcut.activated.connect(self.save_selection)

        # Create a keyboard shortcut for closing the program
        self.close_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self)
        self.close_shortcut.activated.connect(self.close)

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
            x1, y1, x2, y2 = self.get_selected_area_coordinates()
            selected_area = self.screenshot.copy(x1, y1, x2 - x1, y2 - y1)
            selected_area.save("screenshot_selection.png")
    
    def copy_selection(self):
        if self.selection_start is not None and self.selection_end is not None:
            x1, y1, x2, y2 = self.get_selected_area_coordinates()
            selected_area = self.screenshot.copy(x1, y1, x2 - x1, y2 - y1)

            # Save the selected area to the clipboard
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setImage(selected_area)

    def get_selected_area_coordinates(self):
        # Calculate the coordinates of the selected area
        x1 = min(self.selection_start.x(), self.selection_end.x())
        y1 = min(self.selection_start.y(), self.selection_end.y())
        x2 = max(self.selection_start.x(), self.selection_end.x())
        y2 = max(self.selection_start.y(), self.selection_end.y())
        return x1, y1, x2, y2

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ScreenshotWindow()
    window.show()
    app.exec_()
