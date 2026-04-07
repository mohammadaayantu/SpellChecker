# entry point
# runs the spell checker program

from spell_checker import load_dictionary, check_word, get_suggestions
from input_handler import KeyboardInput, TextFileInput, CSVInput


def choose_input():
    # menu
    # choose input type
    print("Choose input method:")
    print("1. Keyboard")
    print("2. Text file")
    print("3. CSV file")

    choice = input("Enter choice: ")

    if choice == "1":
        return KeyboardInput()
    elif choice == "2":
        return TextFileInput()
    elif choice == "3":
        return CSVInput()
    else:
        print("Invalid choice, using keyboard")
        return KeyboardInput()


def main():
    print("Simple Spell Checker")

    # setup
    dictionary = load_dictionary("data/dictionary.txt")

    # input
    input_handler = choose_input()
    words = input_handler.get_words()

    # processing
    for word in words:
        if check_word(word, dictionary):
            print(word, "is correct")
        else:
            print(word, "is incorrect")

            suggestions = get_suggestions(word, dictionary)

            if suggestions:
                print("Suggestions:", ", ".join(suggestions))
            else:
                print("No suggestions found")


# entry point
# start program
if __name__ == "__main__":
    main()