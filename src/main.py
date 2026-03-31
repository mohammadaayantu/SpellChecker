from spell_checker import load_dictionary, check_word
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

 m
if __name__ == "__main__":
    main()