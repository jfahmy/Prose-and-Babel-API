import markov
import pronouncing
import random
import nltk

url = "http://www.gutenberg.org/cache/epub/996/pg996.html"

chain = markov.build_chain(url)

print(random.choice(list(chain)))
# pronouncing.rhymes("climbing")


d = cmudict.dict()
def count_syllables_in_sentence(sentence):
    counter = 0
    for word in sentence:
        counter += [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    return counter


def generate_sentence(full_text):
    sentence = []
    word = random.choice(chain["NONWORD"])
    sentence.append(word)

    while chain[word] != ["NONWORD"]:
        word = random.choice(chain[word])
        sentence.append(word)

    sentence = ' '.join(sentence)
    return sentence


def build_line(num, words):
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
