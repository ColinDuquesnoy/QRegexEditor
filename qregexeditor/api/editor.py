"""
This module contains the editor widget implementation.
"""
from pyqode.core.qt import QtWidgets
from .forms import editor_ui


class RegexEditorWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = editor_ui.Ui_Form()
        self.ui.setupUi(self)

    def showEvent(self, ev):
        super().showEvent(ev)
        self.ui.groupCheatSheet.hide()
