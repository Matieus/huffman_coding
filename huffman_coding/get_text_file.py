class GetTextFile():
    def __init__(self):
        with open("text.txt", "r") as file:
            self.file = file.read()

    def get_text(self):
        return self.file
