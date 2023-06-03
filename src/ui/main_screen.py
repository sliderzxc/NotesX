from PyQt6.QtWidgets import QApplication, QWidget
import sys


def launch():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()
