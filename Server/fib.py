import random
import re
import nltk
import requests
import requests
from bs4 import BeautifulSoup

from nltk.corpus import cmudict
dictionary = cmudict.dict()

def read_file():
    with open('poem_archive.txt', mode="r") as all_words:
        lines = all_words.read().split("\n")
        lines_with_end = []
        for line in lines:
            if line != "":
                line = line + " ENDLINE"
                lines_with_end.append(line)
        lines = " ".join(lines_with_end)
        all_words = lines.split()
        words = []
        for word in all_words:
            word = clean_word(word)
            if word in dictionary or word == "I" or word == "ENDLINE":
                words.append(word)

        return words


def clean_word(word):
        word = re.sub(r'\W+', '', word)
        return word


d = cmudict.dict()
def count_syllables_in_sentence(sentence):
    counter = 0
    # string = re.sub(r'-','', sentence)
    for word in sentence:
        if word != "-":
            counter += [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    return counter



def build_line(num, words):
    parts_of_speech = ['CC', 'PRP', 'PRP$', 'DT', 'IN']
    filler = ['and', 'the', 'that', 'their', 'o', 'they', 'did', 'to', 'of', 'he',
    'she', 'thy', 'for', 'or', 'are', 'were', 'her', 'his']
    index = random.randint(0,len(words)-1)
    while words[index] == 'ENDLINE' or nltk.pos_tag(words[index])[-1][1] in parts_of_speech or words[index] in filler:
        index = random.randint(0,len(words)-1)

    sentence = []

    while count_syllables_in_sentence(sentence) != num and count_syllables_in_sentence(sentence) < num:
        if words[index] == 'ENDLINE':
            sentence.insert(0, "-")
            index -= 1
        else:
            sentence.insert(0, words[index])
            index -= 1

    if count_syllables_in_sentence(sentence) == num:
        return " ".join(sentence)
    else:
        return "blank"



def get_lines(syllable_counts):
    text = read_file()
    poem = ""
    for count in syllable_counts:
        line = "blank"
        while line == "blank":
            line = build_line(count, text)
            if count < 3:
                line = re.sub(r' -','', line)
            else:
                line = re.sub(r' -',',', line)

        poem += line + "\n"

    return poem

# #
print(get_lines([1,1,2,3,5,8,13]))
# #
#
# # read_file()
# print("of tag:")
# print(nltk.pos_tag("of")[-1][1])
# print("to tag:")
# print(nltk.pos_tag("to")[-1][1])

read_file()
