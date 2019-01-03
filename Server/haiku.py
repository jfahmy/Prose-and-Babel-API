import random
import re
import nltk
from nltk.corpus import cmudict
dictionary = cmudict.dict()

def read_file():
    with open('./Resources/don.txt', mode="r") as all_words:
        all_words = all_words.read().split()
        clean_words = []
        for word in all_words:
            word = clean_word(word)
            if word in dictionary or word == "I":
                clean_words.append(clean_word(word))

        return clean_words

def clean_word(word):
        word = re.sub(r'\W+', '', word)
        return word


d = cmudict.dict()
def count_syllables_in_sentence(sentence):
    counter = 0
    for word in sentence:
        counter += [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    return counter



def build_line(num):
    words = read_file()
    index = random.randint(0,len(words)-1)
    sentence = []

    while count_syllables_in_sentence(sentence) != num and count_syllables_in_sentence(sentence) < num:
        sentence.insert(0, words[index])
        index -= 1

    if count_syllables_in_sentence(sentence) == num:
        # return " ".join(sentence)
        return sentence
    else:
        return "blank"



def build_haiku():
    first = "blank"
    while first == "blank":
        first = build_line(5)
        # print(nltk.pos_tag(first)[-1][1])

    second = "blank"
    while second == "blank":
        second = build_line(7)
        # print(nltk.pos_tag(second)[-1][1])

    third = "blank"
    parts_of_speech = ['CC', 'PRP', 'PRP$', 'DT']
    while third == "blank" :
        third = build_line(5)
        # print(nltk.pos_tag(third)[-1][1])
        if nltk.pos_tag(third)[-1][1] in parts_of_speech:
            third = "blank"

    return " ".join(first) + "\n" + " ".join(second) + "\n" + " ".join(third)
