import random
import re
import nltk
import requests
import requests
from bs4 import BeautifulSoup

from nltk.corpus import cmudict
dictionary = cmudict.dict()

def read_file():
    with open('Prose-and-Babel-API/poem_archive.txt', mode="r") as all_words:
        lines = all_words.read().split("\n")
        lines_with_end = []
        for line in lines:
            if line != "":
                line = line + " ENDLINE"
                lines_with_end.append(line)
        lines = " ".join(lines_with_end)

        return clean_words(lines)


def clean_word(word):
        word = re.sub(r'\W+', '', word)
        return word


def clean_words(lines):
    all_words = lines.split()
    words = []
    for word in all_words:
        word = clean_word(word)
        if word in dictionary or word == "I" or word == "ENDLINE":
            words.append(word)

    return words

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
    'she', 'thy', 'for', 'or', 'are', 'were', 'her', 'his', 'as']
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



def get_lines(text="blank"):
    if text == "blank":
        text = read_file()
    else:
        text = clean_words(text)
    poem = ""
    syllable_counts = [1,1,2,3,5,8,13]
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


get_lines()
# #
# print(get_lines([1,1,2,3,5,8,13]))
# #
#
# # read_file()
# print("of tag:")
# print(nltk.pos_tag("of")[-1][1])
# print("to tag:")
# print(nltk.pos_tag("to")[-1][1])



# def match_class(target):
#     def do_match(tag):
#         classes = tag.get('class', [])
#         return all(c in classes for c in target)
#     return do_match
#
#
#
# ebook_url = "https://www.gutenberg.org/files/15553/15553-h/15553-h.htm"
# response = requests.get(ebook_url)
#
# text = response.text
#
#
# text_archive = open("poem_archive.txt", "w")
#
# soup = BeautifulSoup(text, 'html.parser')
# # soup = BeautifulSoup(text)
# for span in soup.find_all(match_class(["poem"])):
#     text_archive.write(span.get_text())

# for span in soup.find_all('poem'):
    # text_archive.write(span.get_text())
