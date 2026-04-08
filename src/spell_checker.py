def load_dictionary(file_path):
    try:
        with open(file_path, "r") as file:
            return set(word.strip().lower() for word in file)
    except FileNotFoundError:
        print("Dictionary file not found")
        return set()

# check if word is correct
def check_word(word, dictionary):
    return word.lower() in dictionary

 
def get_suggestions(word, dictionary):
    letters = "abcdefghijklmnopqrstuvwxyz"
    word = word.lower()
    suggestions = set()

    # deletion
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in dictionary:
            suggestions.add(new_word)

    # insertion
    for i in range(len(word) + 1):
        for letter in letters:
            new_word = word[:i] + letter + word[i:]
            if new_word in dictionary:
                suggestions.add(new_word)

    # substitution
    for i in range(len(word)):
        for letter in letters:
            new_word = word[:i] + letter + word[i+1:]
            if new_word in dictionary:
                suggestions.add(new_word)

    # transposition
    for i in range(len(word) - 1):
        new_word = word[:i] + word[i+1] + word[i] + word[i+2:]
        if new_word in dictionary:
            suggestions.add(new_word)

     
    return sorted(list(suggestions))[:5]