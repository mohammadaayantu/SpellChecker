def load_dictionary(file_path):
    with open(file_path, "r") as file:
        return set(word.strip().lower() for word in file)

# check if word is in dictionary
def check_word(word, dictionary):
    return word.lower() in dictionary