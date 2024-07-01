# Logger.py - Logger class

class Logger():
    def __init__(self):
        self.file = open("log.txt", "a")
        self.file.write(f"--Debut log--\n")
        self.counter = 0
    
    def __del__(self):
        self.file.write(f"--Fin log: {self.counter} log(s)--\n")
        self.file.close()

    def log(self, message):
        self.counter += 1
        self.file.write(f"{message}\n")


class Test():
    def __init__(self):
        self.logger = Logger()
    def appel(self, message):
        self.logger.log(message)


if __name__ == "__main__":
    test = Test()
    for i in range(1, 6):
        if i == 1:
            test.appel("1er Appel")
        else:
            test.appel(f"{i}eme Appel")