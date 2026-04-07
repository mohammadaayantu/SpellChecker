class InputHandler:
    def get_words(self):
        pass

# user types words
class KeyboardInput(InputHandler):

    def get_words(self):
        user_input = input("Enter words: ")
        return user_input.split()

# reads words from txt file
class TextFileInput(InputHandler):

    def get_words(self):
        file_name = input("Enter text file name: ")

        with open("data/" + file_name, "r") as file:
            return file.read().split()

# reads first column
class CSVInput(InputHandler):

    def get_words(self):
        import csv

        file_name = input("Enter CSV file name: ")

        with open("data/" + file_name, "r") as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]