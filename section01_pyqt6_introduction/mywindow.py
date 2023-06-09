from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget


import sys

# Create an application
app = QApplication(sys.argv)
# Create a window
window = QMainWindow()
window.statusBar().showMessage('Hello World')
window.menmuBar().addMenu("&File")
# Set window size
window.show()
# Set window title
sys.exit(app.exec())


#QToolBars, QDialog,