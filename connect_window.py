# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ConnectWindow(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(401, 211)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.server_input = QtGui.QLineEdit(self.gridLayoutWidget)
        self.server_input.setObjectName(_fromUtf8("server_input"))
        self.gridLayout.addWidget(self.server_input, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.port_input = QtGui.QLineEdit(self.gridLayoutWidget)
        self.port_input.setObjectName(_fromUtf8("port_input"))
        self.gridLayout.addWidget(self.port_input, 0, 3, 1, 1)
        self.channel_input = QtGui.QLineEdit(self.gridLayoutWidget)
        self.channel_input.setObjectName(_fromUtf8("channel_input"))
        self.gridLayout.addWidget(self.channel_input, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 381, 71))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.nickname_input = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.nickname_input.setObjectName(_fromUtf8("nickname_input"))
        self.gridLayout_3.addWidget(self.nickname_input, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 4, 1, 1)
        self.realname_input = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.realname_input.setObjectName(_fromUtf8("realname_input"))
        self.gridLayout_3.addWidget(self.realname_input, 0, 3, 1, 1)
        self.ident_input = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.ident_input.setObjectName(_fromUtf8("ident_input"))
        self.gridLayout_3.addWidget(self.ident_input, 0, 5, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 381, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.connect_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.connect_btn.setObjectName(_fromUtf8("connect_btn"))
        self.horizontalLayout.addWidget(self.connect_btn)
        self.reset_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.reset_btn.setObjectName(_fromUtf8("reset_btn"))
        self.horizontalLayout.addWidget(self.reset_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.close_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.horizontalLayout.addWidget(self.close_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_3.setText(_translate("Form", "Channel:", None))
        self.label_2.setText(_translate("Form", "Port:", None))
        self.label.setText(_translate("Form", "Server:", None))
        self.label_4.setText(_translate("Form", "Nickname:", None))
        self.label_5.setText(_translate("Form", "Real name:", None))
        self.label_6.setText(_translate("Form", "Ident:", None))
        self.connect_btn.setText(_translate("Form", "Connect", None))
        self.reset_btn.setText(_translate("Form", "Reset", None))
        self.close_btn.setText(_translate("Form", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_ConnectWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

