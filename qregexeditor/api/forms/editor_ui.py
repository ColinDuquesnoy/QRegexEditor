# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Development/QRegexEditor/forms/editor.ui'
#
# Created: Thu Aug  7 11:06:54 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 377)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lblError = QtWidgets.QLabel(self.groupBox)
        self.lblError.setStyleSheet("color: #FF0000;")
        self.lblError.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblError.setContentsMargins(5, 5, 5, 5)
        self.lblError.setObjectName("lblError")
        self.gridLayout.addWidget(self.lblError, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditRegex = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditRegex.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEditRegex.setObjectName("lineEditRegex")
        self.horizontalLayout_2.addWidget(self.lineEditRegex)
        self.checkBoxIgnoreCase = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxIgnoreCase.setObjectName("checkBoxIgnoreCase")
        self.horizontalLayout_2.addWidget(self.checkBoxIgnoreCase)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEditTestString = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEditTestString.setMinimumSize(QtCore.QSize(400, 0))
        self.plainTextEditTestString.setObjectName("plainTextEditTestString")
        self.gridLayout_2.addWidget(self.plainTextEditTestString, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEditMatchResult = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.plainTextEditMatchResult.setMinimumSize(QtCore.QSize(400, 0))
        self.plainTextEditMatchResult.setReadOnly(True)
        self.plainTextEditMatchResult.setObjectName("plainTextEditMatchResult")
        self.gridLayout_3.addWidget(self.plainTextEditMatchResult, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.checkBoxQuickRef = QtWidgets.QCheckBox(Form)
        self.checkBoxQuickRef.setObjectName("checkBoxQuickRef")
        self.verticalLayout.addWidget(self.checkBoxQuickRef)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Regular expression"))
        self.lblError.setText(_translate("Form", "lblError"))
        self.lineEditRegex.setToolTip(_translate("Form", "<html><head/><body><p>Type your regular expression here</p></body></html>"))
        self.checkBoxIgnoreCase.setToolTip(_translate("Form", "<html><head/><body><p>Perform case-insensitive matching; expressions like <span style=\" font-family:\'Courier New,courier\';\">[A-Z]</span> will match lowercase letters, too. This is not affected by the current locale.</p></body></html>"))
        self.checkBoxIgnoreCase.setText(_translate("Form", "Ignore case"))
        self.groupBox_2.setTitle(_translate("Form", "Test strings"))
        self.plainTextEditTestString.setToolTip(_translate("Form", "<html><head/><body><p>Type your test strings here</p></body></html>"))
        self.groupBox_3.setTitle(_translate("Form", "Match result"))
        self.plainTextEditMatchResult.setToolTip(_translate("Form", "<html><head/><body><p>The match result</p></body></html>"))
        self.checkBoxQuickRef.setToolTip(_translate("Form", "<html><head/><body><p>Show/Hide the quick reference panel.</p></body></html>"))
        self.checkBoxQuickRef.setText(_translate("Form", "Show Regular Expression Quick Reference"))
