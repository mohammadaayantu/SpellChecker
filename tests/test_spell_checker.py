# allow tests to access src folder
import sys
import os
sys.path.append(os.path.abspath("SpellChecker/src"))

from spell_checker import load_dictionary, check_word, get_suggestions

# dictionary loads correctly
def test_dictionary_loading():
    dictionary = load_dictionary("SpellChecker/data/dictionary.txt")
    assert "cat" in dictionary


# correct word returns True
def test_correct_word():
    dictionary = {"cat", "dog"}
    assert check_word("cat", dictionary)


# incorrect word returns False
def test_incorrect_word():
    dictionary = {"cat", "dog"}
    assert not check_word("bat", dictionary)


# suggestions are generated
def test_suggestions():
    dictionary = {"cat", "bat", "rat"}
    suggestions = get_suggestions("dat", dictionary)
    assert "cat" in suggestions


# no suggestions case
def test_no_suggestions():
    dictionary = {"cat", "dog"}
    suggestions = get_suggestions("zzz", dictionary)
    assert suggestions == []


# empty word handled
def test_empty_word():
    dictionary = {"cat"}
    suggestions = get_suggestions("", dictionary)
    assert isinstance(suggestions, list)

# blank input (user presses enter)
def test_blank_input():
    dictionary = {"cat"}
    word = ""
    assert not check_word(word, dictionary)


# uppercase input
def test_uppercase_input():
    dictionary = {"cat"}
    assert check_word("CAT", dictionary)


# mixed case input
def test_mixed_case_input():
    dictionary = {"hello"}
    assert check_word("HeLLo", dictionary)


# word with numbers
def test_word_with_numbers():
    dictionary = {"cat"}
    assert not check_word("cat123", dictionary)


# single letter word
def test_single_letter():
    dictionary = {"a", "i"}
    assert check_word("a", dictionary)


# long word should not crash
def test_long_word():
    dictionary = {"cat"}
    word = "aaaaaaaaaaaaaaaaaaaa"
    suggestions = get_suggestions(word, dictionary)
    assert isinstance(suggestions, list)


# no duplicate suggestions
def test_no_duplicate_suggestions():
    dictionary = {"cat"}
    suggestions = get_suggestions("cta", dictionary)
    assert len(suggestions) == len(set(suggestions))


# suggestion limit (max 5)
def test_suggestion_limit():
    dictionary = {"cat", "bat", "rat", "hat", "mat", "sat", "pat"}
    suggestions = get_suggestions("dat", dictionary)
    assert len(suggestions) <= 5

 
# punctuation in word
def test_word_with_punctuation():
    dictionary = {"cat"}
    assert not check_word("cat!", dictionary)


# spaces inside word
def test_word_with_spaces():
    dictionary = {"cat"}
    assert not check_word("c a t", dictionary)


# leading/trailing spaces
def test_word_with_extra_spaces():
    dictionary = {"cat"}
    assert check_word("  cat  ".strip(), dictionary)


# empty dictionary
def test_empty_dictionary():
    dictionary = set()
    assert not check_word("cat", dictionary)


# suggestions with empty dictionary
def test_suggestions_empty_dictionary():
    dictionary = set()
    suggestions = get_suggestions("cat", dictionary)
    assert suggestions == []


# repeated letters case
def test_repeated_letters():
    dictionary = {"book"}
    suggestions = get_suggestions("bok", dictionary)
    assert isinstance(suggestions, list)


# correct word suggestions still safe
def test_correct_word_no_suggestions_needed():
    dictionary = {"cat"}
    suggestions = get_suggestions("cat", dictionary)
    assert isinstance(suggestions, list)


# numeric only input
def test_numeric_only():
    dictionary = {"cat"}
    assert not check_word("12345", dictionary)


# special characters only
def test_special_characters_only():
    dictionary = {"cat"}
    assert not check_word("@@@", dictionary)


# large dictionary lookup
def test_large_dictionary_lookup():
    dictionary = {str(i) for i in range(1000)}
    assert check_word("500", dictionary)


# suggestion consistency
def test_suggestion_consistency():
    dictionary = {"cat", "bat", "rat"}
    s1 = get_suggestions("dat", dictionary)
    s2 = get_suggestions("dat", dictionary)
    assert s1 == s2


# case handling in suggestions
def test_suggestion_case_handling():
    dictionary = {"cat"}
    suggestions = get_suggestions("CAT", dictionary)
    assert isinstance(suggestions, list)