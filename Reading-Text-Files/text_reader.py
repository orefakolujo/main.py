# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

Word_dictionary = {}


def read_file_content(story):
    # opens the story file and returns its content
    with open(story, 'r') as f:
        content = f.read()
        return content


def count_words():
    text = read_file_content("./story.txt")
    punctuations = ".,!?"
    for word in text.split():
        for punc in punctuations:
            if punc in word:
                word = word.replace(punc, "")

        Word_dictionary[word] = text.split().count(word)

    print(Word_dictionary)


count_words()
