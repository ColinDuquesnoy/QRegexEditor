"""
Contains the quick reference widget
"""
import re
from pyqode.qt import QtCore, QtWidgets
from .forms import quick_ref_ui

class QuickRefWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QuickRefWidget, self).__init__(parent)
        self.ui = quick_ref_ui.Ui_Form()
        self.ui.setupUi(self)
        self._fix_default_font_size()
        self._setup_context_menu()

    def _fix_default_font_size(self):
        # remove fixed font size to allow the user to zoom in/out using
        # Ctrl+Mouse Wheel
        # Note: Zooming into HTML documents only works if the font-size is not
        # set to a fixed size.
        # (source: http://qt-project.org/doc/qt-5/qtextedit.html)
        html = self.ui.textEditQuickRef.toHtml()
        html = re.sub('font-size:\d+pt;', '', html)
        self.ui.textEditQuickRef.setHtml(html)

    def _setup_context_menu(self):
        self.ui.textEditQuickRef.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.ui.textEditQuickRef.customContextMenuRequested.connect(
            self._show_context_menu)
        self.context_menu = self.ui.textEditQuickRef.createStandardContextMenu()
        self.context_menu.addSeparator()
        action = self.context_menu.addAction('Zoom in')
        action.setShortcut('Ctrl+i')
        action.triggered.connect(self.ui.textEditQuickRef.zoomIn)
        self.addAction(action)
        action = self.context_menu.addAction('Zoom out')
        action.setShortcut('Ctrl+o')
        self.addAction(action)
        action.triggered.connect(self.ui.textEditQuickRef.zoomOut)

    def _show_context_menu(self, pos):
        self.context_menu.exec_(self.ui.textEditQuickRef.mapToGlobal(pos))
