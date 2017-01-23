from html.parser import HTMLParser

from Messages import *


# returns all the class attribute types
def get_classes_attr(attrs):
    return [a[1] for a in attrs if a[0] == "class"]


# Parser for the messages html
class MessageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.div_count = 0

        self.threads = []
        self.thread = None  # Current thread we are working on
        self.thread_div_count = -1

        self.message = None  # Current message we are working on
        self.p_message = None
        self.message_div_count = -1

    def error(self, message):
        print("Error: " + message)

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            self.div_count += 1
            if "thread" in get_classes_attr(attrs):  # start of thread
                print("Start Thread:", len(self.threads) + 1)  # useful to make sure the parser is actually running
                self.thread = MessageThread()
                self.thread_div_count = self.div_count
            elif "message" in get_classes_attr(attrs):  # start of message
                self.message = Message()
                self.message_div_count = self.div_count
        elif tag == "span":
            if "user" in get_classes_attr(attrs):
                self.message.parse_user = True
            elif "meta" in get_classes_attr(attrs):
                self.message.parse_meta = True

    def handle_endtag(self, tag):
        if tag == "div":
            if self.div_count == self.thread_div_count:
                self.threads.append(self.thread)
                self.thread = None
                self.thread_div_count = -1
            elif self.div_count == self.message_div_count:
                self.thread.add_message(self.message)
                self.p_message = self.message
                self.message = None
                self.message_div_count = -1
            self.div_count -= 1

    def handle_data(self, data):
        if self.thread is not None and not self.thread.thread_initialize:
            self.thread.set_name(data)
        elif self.message is not None:
            if self.message.parse_user:
                self.message.set_user(data)
            elif self.message.parse_meta:
                self.message.set_meta(data)
        elif self.p_message is not None:
            self.p_message.set_data(data)
            self.p_message = None

    def get_threads(self):
        return self.threads
