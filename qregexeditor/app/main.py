"""
Application entry point
"""
import sys
from pyqode.qt import QtWidgets
from .main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
