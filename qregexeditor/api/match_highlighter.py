import re
from pyqode.core.qt import QtGui


class MatchHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.prog = None
        self._format = QtGui.QTextCharFormat()
        self._format.setBackground(QtGui.QBrush(QtGui.QColor('#bbfcbb')))

    def highlightBlock(self, text):
        if self.prog:
            match = self.prog.search(text)
            while match:
                start, end = match.span()
                self.setFormat(start, end - start, self._format)
                match = self.prog.search(text, match.end())

