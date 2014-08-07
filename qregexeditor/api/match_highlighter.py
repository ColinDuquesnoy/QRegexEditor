import re
from pyqode.core.qt import QtGui


class MatchHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.prog = None
        self._format = QtGui.QTextCharFormat()
        self._format.setBackground(QtGui.QBrush(QtGui.QColor('#bbfcbb')))

    def highlightBlock(self, text):
        if self.prog and text:
            match = self.prog.search(text)
            if match:
                start, end = match.span()
                while match and end > start:
                    self.setFormat(start, end - start, self._format)
                    match = self.prog.search(text, match.end())
                    if match:
                        start, end = match.span()

