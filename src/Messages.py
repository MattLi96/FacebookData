"""The data format to use to store messages"""


class MessageThread:
    def __init__(self):
        self.name = ""  # name of the message thread
        self.thread_initialize = False  # if thread has been initialized
        self.participants = []
        self.messages = []

    def set_name(self, name):
        self.name = name
        self.participants = [n.strip() for n in name.split(",")]
        self.thread_initialize = True

    def add_message(self, message):
        self.messages.append(message)


class Message:
    def __init__(self):
        self.user = ""  # user who sent the message
        self.meta = ""  # meta information about the message, usually time
        self.data = ""  # the actual data of the message
        self.parse_user = False
        self.parse_meta = False

    def set_user(self, user):
        self.user = user
        self.parse_user = False

    def set_meta(self, meta):
        self.meta = meta
        self.parse_meta = False

    def set_data(self, data):
        self.data += data
