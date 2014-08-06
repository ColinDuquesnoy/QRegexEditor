"""
Application entry point
"""
import sys
from pyqode.core.qt import QtWidgets
from qregexeditor.api import RegexEditorWidget


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("QRegexEditor")
    editor = RegexEditorWidget()
    window.setCentralWidget(editor)
    window.show()
    app.exec_()
