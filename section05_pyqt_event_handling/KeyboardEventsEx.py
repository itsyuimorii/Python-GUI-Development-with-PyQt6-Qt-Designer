from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("Handling Keyboard Events")

        self.label = QLabel("Please give best rating for the course", self)
        self.label.setFont(QFont("Times", 15))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        self.label.move(200,200)


    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key.Key_Up:
            self.label.move(self.label.x(), self.label.y() - 10)
        elif key == Qt.Key.Key_Down:
            self.label.move(self.label.x(), self.label.y() + 10)

        elif key == Qt.Key.Key_Left:
            self.label.move(self.label.x() - 10, self.label.y())

        elif key == Qt.Key.Key_Right:
            self.label.move(self.label.x() + 10, self.label.y())

        elif key == Qt.Key.Key_Escape:
            self.close()

    def keyReleaseEvent(self, event):
        text = event.text()
        print("Key released : " , text)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())