"""
This package a pyqt distutils hook to replace PyQt5 by our own (
qregexeditor.qt).
"""


def fix_qt_imports(path):
    with open(path, 'r') as f_script:
        lines = f_script.read().splitlines()
    new_lines = []
    for l in lines:
        if l.startswith("import "):
            l = "from . " + l
        if "from PyQt5 import" in l:
            l = l.replace("from PyQt5 import", "from qregexeditor.qt import")
        new_lines.append(l)
    with open(path, 'w') as f_script:
        f_script.write("\n".join(new_lines))
