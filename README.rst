QRegexEditor
============

QRegexEditor is a **simple** regular expression editor written in Python 3 and
PyQt.

You can use QRegexEditor as a standalone application but also as a widget
in your own PyQt/PySide application.

Installation
------------

::

pip3 install qregexeditor


Dependencies
------------
  - python 3
  - PyQt5 or PySide or PyQt4
  - pyqode.qt


Using the widget in a custom PyQt application
---------------------------------------------

Use the widget as any other qt widget.

You may specify the regular expression and the string pattern programmatically.
You might also want to connect to the ``quick_ref_requested`` signal so that your
application can show/hide a quick reference widget in the most appropriate place.


.. code-block:: python

    import sys
    from qregexeditor.api import RegexEditorWidget, QuickRefWidget
    from PyQt4.QtGui import QApplication, QMainWindow


    app = QApplication(sys.argv)
    window = QMainWindow()
    editor = RegexEditorWidget()
    quick_ref = QuickRefWidget()
    quick_ref.hide()
    window.setCentralWidget(editor)
    # show/hide quick reference widget
    editor.quick_ref_requested.connect(quick_ref.setVisible)
    window.show()
    app.exec_()
