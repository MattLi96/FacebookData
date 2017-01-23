"""The data format to use to store messages"""

from TimeParser import parse_datetime
from Username import get_username, finder


# A complete log of all messages. Initializing this does final processing on a list of message threads.
class MessageLog:
    def __init__(self, threads):
        initial_log = {}  # dictionary from participants to a list of corresponding threads
        print("Cleaning up usernames")
        for p_thread in threads:
            thread = MessageThread(p_thread)
            if thread.participants in initial_log:
                initial_log[thread.participants].append(thread)
            else:
                initial_log[thread.participants] = [thread]

        # consolidate message threads by participants
        print("Consolidating messages")
        self.log = {}  # The full log, participants to messages
        for p, m_threads in initial_log.items():
            self.log[p] = [m for t in m_threads for m in t.messages]

        # sort messages by time
        for p, m_thread in self.log.items():
            self.log[p] = sorted(m_thread, key=lambda message: message.date_time)

        print("Unknown IDs:", finder.unknown)  # Printout the ids that were could not be found, must manually check

    # Log is a dictionary from participants to a list of messages
    def get_log(self):
        return self.log


# A set of messages between a group of participants
class MessageThread:
    def __init__(self, parse_thread):
        self.participants = frozenset(get_username(p) for p in parse_thread.participants)
        self.messages = [Message(m) for m in parse_thread.messages]


# A single message and it's metadata
class Message:
    def __init__(self, parse_message):
        self.sender = get_username(parse_message.user)  # user who sent the message
        self.date_time = parse_datetime(parse_message.meta)  # date-time when message was sent
        self.data = parse_message.data  # the actual data of the message
