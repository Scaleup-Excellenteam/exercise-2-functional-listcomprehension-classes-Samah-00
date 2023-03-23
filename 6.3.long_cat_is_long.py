import re

text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

# remove non-alphabetic characters from the text using regular expressions
text = re.sub('[^a-zA-Z\\s]+', '', text)
# create a set of the text's words using set comprehension
words = {word for word in text.lower().split() if word.isalpha()}
# create a dict [word: len(word] from the set "words" using dictionary comprehension
words_count = {word: len(word) for word in words}
print(words_count)
