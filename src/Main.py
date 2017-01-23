"""Run This!"""
from Parser import MessageParser

messages_data_file = "../data/html/messages.htm"
processed_messages_file = "../out/message_log.txt"

if __name__ == '__main__':
    file = open(messages_data_file, 'r', encoding="utf8")
    parser = MessageParser()
    parser.feed(file.read())
    log = parser.get_message_log()
    log.save(processed_messages_file)
