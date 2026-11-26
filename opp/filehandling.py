class Report:
    def __init__(self, filename):
        self.file = open(filename, "w")
        print("File opened")

    def write_data(self, text):
        self.file.write(text)

    def __del__(self):
        self.file.close()
        print("File closed")


f1 = Report("report.txt")
f1.write_data("Python constructor")

del f1

with open("report.txt", "r") as file:
    print(file.read())