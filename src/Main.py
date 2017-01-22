from Parser import MessageParser

messages_data_file = "../data/html/messages.htm"

if __name__ == '__main__':
    file = open(messages_data_file, 'r', encoding="utf8")
    parser = MessageParser()
    parser.feed(file.read())

    print([thread.name for thread in parser.get_threads()])
