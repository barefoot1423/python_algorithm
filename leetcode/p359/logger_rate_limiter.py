class Logger:

    def __init__(self):
        self.dic = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message in self.dic and self.dic[message] + 10 <= timestamp:
            self.dic[message] = timestamp
            return True
        elif message not in self.dic:
            self.dic[message] = timestamp
            return True
        else:
            return False


logger = Logger()
logger.shouldPrintMessage(1, "foo")
logger.shouldPrintMessage(2, "bar")
logger.shouldPrintMessage(3, "foo")
logger.shouldPrintMessage(8, "bar")
logger.shouldPrintMessage(10, "foo")
logger.shouldPrintMessage(11, "foo")

print(logger.dic.items())