"""
Contains the quick reference widget
"""
from pyqode.qt import QtWidgets
from .forms import quick_ref_ui

class QuickRefWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = quick_ref_ui.Ui_Form()
        self.ui.setupUi(self)
