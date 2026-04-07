# runs the spell checker program

from spell_checker import load_dictionary, check_word, get_suggestions
from input_handler import get_words


def main():
    print("Simple Spell Checker")

    # load dictionary
    dictionary = load_dictionary("data/dictionary.txt")

    # get words from user
    words = get_words()

    # check each word
    for word in words:
        if check_word(word, dictionary):
            print(word, "is correct")
        else:
            print(word, "is incorrect")

            # suggestions
            suggestions = get_suggestions(word, dictionary)

            if suggestions:
                print("Suggestions:", ", ".join(suggestions))
            else:
                print("No suggestions found")


# start program
if __name__ == "__main__":
    main()