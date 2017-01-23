"""The data format to use to store messages"""
import copy

from TimeParser import parse_datetime
from Username import *

finder = UsernameFinder()


# gets the username for a string
def get_username(string):
    return finder.get_username(extract_uid(string)) if "@facebook" in string else string


# A complete log of all messages. Initializing this does final processing on a list of message threads.
class MessageLog:
    def __init__(self, threads):
        threads = copy.deepcopy(threads)  # deep copy the input list, mutations will be made to the elements
        # convert facebook ids to username
        # consolidate message threads by participants
        # sort messages in each

        for p_thread in threads:
            thread = MessageThread(p_thread)

        print(finder.uid_to_name)
        print(finder.unknown)


# A set of messages between a group of participants
class MessageThread:
    def __init__(self, parse_thread):
        self.participants = {get_username(p) for p in parse_thread.participants}
        self.messages = [Message(m) for m in parse_thread.messages]


# A single message and it's metadata
class Message:
    def __init__(self, parse_message):
        self.sender = get_username(parse_message.user)  # user who sent the message
        self.date_time = parse_datetime(parse_message.meta)  # date-time when message was sent
        self.data = parse_message.data  # the actual data of the message
