from spell_checker import load_dictionary, check_word, get_suggestions
from input_handler import KeyboardInput, TextFileInput, CSVInput
# choose input type
def choose_input():
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
    dictionary = load_dictionary("SpellChecker/data/dictionary.txt")

    if not dictionary:
        print("No dictionary loaded. Exiting.")
        return

    # input
    input_handler = choose_input()
    words = input_handler.get_words()

    if not words:
        print("No words to check")
        return

    # processing
    print("\nChecking spelling...\n")

    for word in words:
        if check_word(word, dictionary):
            print(f"{word} is correct")
        else:
            print(f"{word} is incorrect")

            suggestions = get_suggestions(word, dictionary)

            if suggestions:
                print("Suggestions:", ", ".join(suggestions))
            else:
                print("No suggestions found")

            print()  # spacing

 
if __name__ == "__main__":
    main()