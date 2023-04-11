class File:
    def __init__(self, file):
        self.file = file

    def clear(self):
        open(self.file, 'w+')

    def read(self):
        file = open(self.file, 'r', -1, 'utf-8')
        return file.read()

    def write(self, text):
        file = open(self.file, 'a+', -1, 'utf-8')
        file.write(text)
