# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout1 = QtGui.QHBoxLayout()
        self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
        self.chat_tabs = QtGui.QTabWidget(self.centralwidget)
        self.chat_tabs.setTabsClosable(True)
        self.chat_tabs.setMovable(False)
        self.chat_tabs.setObjectName(_fromUtf8("chat_tabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.server_output = QtGui.QTextEdit(self.tab)
        self.server_output.setObjectName(_fromUtf8("server_output"))
        self.horizontalLayout.addWidget(self.server_output)
        self.chat_tabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.channel_output = QtGui.QTextEdit(self.tab_2)
        self.channel_output.setObjectName(_fromUtf8("channel_output"))
        self.horizontalLayout_3.addWidget(self.channel_output)
        self.chat_tabs.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout1.addWidget(self.chat_tabs)
        self.user_list = QtGui.QListWidget(self.centralwidget)
        self.user_list.setMinimumSize(QtCore.QSize(0, 0))
        self.user_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.user_list.setObjectName(_fromUtf8("user_list"))
        self.horizontalLayout1.addWidget(self.user_list, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.horizontalLayout2 = QtGui.QHBoxLayout()
        self.horizontalLayout2.setObjectName(_fromUtf8("horizontalLayout2"))
        self.chat_input = QtGui.QLineEdit(self.centralwidget)
        self.chat_input.setObjectName(_fromUtf8("chat_input"))
        self.horizontalLayout2.addWidget(self.chat_input)
        self.send_btn = QtGui.QPushButton(self.centralwidget)
        self.send_btn.setFlat(False)
        self.send_btn.setObjectName(_fromUtf8("send_btn"))
        self.horizontalLayout2.addWidget(self.send_btn)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.chat_tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.chat_tabs.setTabText(self.chat_tabs.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.chat_tabs.setTabText(self.chat_tabs.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.send_btn.setText(_translate("MainWindow", "Send", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

