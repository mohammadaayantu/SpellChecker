from pathlib import Path


class InputHandler:
    def get_words(self):
        pass


# keyboard input
class KeyboardInput(InputHandler):

    def get_words(self):
        user_input = input("Enter words: ")

        if not user_input.strip():
            print("No input given")
            return []

        return user_input.split()


# text file input
class TextFileInput(InputHandler):

    def get_words(self):
        file_name = input("Enter text file name: ")
        data_dir = Path(__file__).resolve().parents[1] / "data"

        try:
            with open(data_dir / file_name, "r") as file:
                return file.read().split()
        except FileNotFoundError:
            print("File not found")
            return []


# csv file input
class CSVInput(InputHandler):

    def get_words(self):
        import csv
        file_name = input("Enter CSV file name: ")
        data_dir = Path(__file__).resolve().parents[1] / "data"

        try:
            with open(data_dir / file_name, "r") as file:
                reader = csv.reader(file)
                return [row[0] for row in reader if row]
        except FileNotFoundError:
            print("File not found")
            return []