"""
Application entry point
"""
import sys
from qregexeditor.qt import QtWidgets
from qregexeditor.app.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
