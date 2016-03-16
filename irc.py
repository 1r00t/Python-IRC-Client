import socket
import string
from PyQt4 import QtCore


class ReadThread(QtCore.QThread):
    new_message_signal = QtCore.pyqtSignal(str)

    def __init__(self, socket):
        QtCore.QThread.__init__(self)
        self.socket = socket

    def run(self):
        readbuffer = ""
        while True:
            readbuffer = readbuffer + self.socket.recv(1024)
            temp = string.split(readbuffer, "\n")
            readbuffer = temp.pop()

            for line in temp:
                line = string.rstrip(line)
                line = string.split(line)

                if(line[0] == "PING"):
                    self.socket.send("PONG %s\r\n" % line[1])
                line = " ".join(line)
                self.new_message_signal.emit(line)

    def stop(self):
        self.exit()


class Client(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.message_queue = Queue()
        self.connected = False
        self.read_thread = ReadThread(self.socket)

    def connect(self, connection_info):
        server = connection_info["server"]
        port = connection_info["port"]
        nickname = connection_info["nickname"]
        ident = connection_info["ident"]
        realname = connection_info["realname"]

        self.socket.connect((server, port))
        self.send("NICK {nickname}".format(nickname=nickname))
        self.send("USER {ident} {server} unused :{realname}".format(
            ident=ident,
            server=server,
            realname=realname))
        self.connected = True

    def join(self, channel):
        self.send("JOIN {channel}".format(channel=channel))

    def send(self, message):
        message = "".join(
            [c for c in message if c in string.ascii_letters
             + string.punctuation + " "])
        self.socket.send(message + "\r\n")
        self.read_thread.new_message_signal.emit(message)

    def disconnect(self):
        self.send("QUIT :bye bye")
        self.socket.close()
        self.connected = False
        self.read_thread.stop()

    def handle_message(self, message):
        # :Ccdc_DuckZ!~duckz@192.153.213.74 PRIVMSG ##linux :hey all, I just wanted to say that I've been updating
        # :mhcerri_!~mhcerri@200-204-219-150.customer.telesp.net.br QUIT :Remote host closed the connection
        line = message.split()
        prefix = ""
        if line[0].startswith(":"):
            prefix = line.pop(0)[1:]
        command = line.pop(0)
        parameters = []
        for i, parameter in enumerate(line):
            if parameter.startswith(":"):
                parameter = parameter[1:]
                parameters.append(" ".join([parameter] + line[i + 1:]))
                break
            parameters.append(parameter)

        return {"prefix": prefix,
                "command": command,
                "parameters": parameters}
