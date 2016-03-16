import sys
from PyQt4 import QtGui
from main_window import Ui_MainWindow
from connect_window import Ui_ConnectWindow
from irc import Client


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.actionConnect.triggered.connect(self.open_connect_window)
        self.actionExit.triggered.connect(self.close)
        self.send_btn.clicked.connect(self.send_message)
        self.chat_input.returnPressed.connect(self.send_message)
        self.connect_window = None
        self.irc = Client()
        self.read_thread = self.irc.read_thread
        self.read_thread.new_message_signal.connect(self.add_new_message)

    def open_connect_window(self):
        if not self.connect_window:
            self.connect_window = ConnectWindow()
            self.connect_window.show()

    def add_new_message(self, message):
        message = unicode(message)
        message_dict = self.irc.handle_message(message)
        prefix = message_dict["prefix"]
        command = message_dict["command"]
        parameters = message_dict["parameters"]
        if command == "PRIVMSG":
            user = prefix.split("!")[0]
            print parameters[0]
            self.channel_output.append("<b>{user}</b>: {text}".format(
                user=user, text=parameters[1]))
        else:
            self.server_output.append(message)

    def send_message(self):
        text = unicode(self.chat_input.text())
        if text:
            self.irc.send("PRIVMSG #testtesttest :" + text)
            self.chat_input.setText("")
            self.chat_input.setFocus()

    def closeEvent(self, event):
        if self.irc.connected:
            self.irc.disconnect()


class ConnectWindow(QtGui.QWidget, Ui_ConnectWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.close_btn.clicked.connect(self.close)
        self.connect_btn.clicked.connect(self.connect)

    def connect(self):
        # for now
        self.server_input.setText("irc.freenode.net")
        self.port_input.setText("6667")
        self.channel_input.setText("#testtesttest")
        self.nickname_input.setText("one_roOt")
        self.ident_input.setText("itsmeeememe")
        self.realname_input.setText("roOt")
        self.update()
        # ^^ for now ^^
        connection_info = {
            "server": str(self.server_input.text()),
            "port": int(str(self.port_input.text())),
            "nickname": str(self.nickname_input.text()),
            "ident": str(self.ident_input.text()),
            "realname": str(self.realname_input.text()),
        }
        channel = str(self.channel_input.text())
        print connection_info, channel
        myapp.irc.connect(connection_info)
        myapp.irc.join(channel)
        myapp.irc.read_thread.start()
        myapp.chat_tabs.setTabText(0, self.server_input.text())
        myapp.chat_tabs.setTabText(1, self.channel_input.text())
        myapp.chat_tabs.setCurrentIndex(1)
        self.close()

    def closeEvent(self, event):
        myapp.connect_window = None


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    myapp.open_connect_window()
    sys.exit(app.exec_())
