import re
from pyqode.qt import QtGui


class MatchHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.prog = None
        self._format = QtGui.QTextCharFormat()
        self._format.setBackground(QtGui.QBrush(QtGui.QColor('#bbfcbb')))

    def highlightBlock(self, text):
        if self.prog and text:
            for m in self.prog.finditer(text):
                start, end = m.span()
                self.setFormat(start, end - start, self._format)
