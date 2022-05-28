# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word_dictionary = {}
anagram_dictionary = {}


def find_anagram(word, anagram):
    for letter in word:
        word_dictionary[letter.lower()] = word.count(letter)

    for letter in anagram:
        anagram_dictionary[letter.lower()] = anagram.count(letter)

    if word_dictionary == anagram_dictionary:
        return True
    else:
        return False


print(find_anagram("elbow", "below"))
