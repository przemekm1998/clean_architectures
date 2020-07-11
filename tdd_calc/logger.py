import datetime


class Logger:
    def __init__(self):
        self.messages = list()

    def log(self, message):
        self.messages.append((datetime.datetime.now(), message))
