from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QPainter, QPen


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Mouse Events")

        self.start_pos = None
        self.end_pos = None


    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.start_pos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.end_pos = event.pos()
            self.update()


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.end_pos = event.pos()
            self.update()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Double Clicked at ", event.pos())



    def wheelEvent(self, event):
        angle = event.angleDelta().y()
        print("Mouse wheel scrolled : ", angle)


    def paintEvent(self, event):
        if self.start_pos and self.end_pos:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.GlobalColor.red))
            painter.drawLine(self.start_pos, self.end_pos)





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())