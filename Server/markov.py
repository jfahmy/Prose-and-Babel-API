import random
import scrape


#Order of 2 chain
def build_chain(content):
    content = content.split()
    chain = {}
    for i,word in enumerate(content):
        if i == len(content) - 3:
            break
        elif i == 0:
            prefix = word + " " + content[i+1]
            chain["NONWORD"] = [prefix]
            suffix = content[i + 2] + " " + content[i + 3]
            chain[prefix] = [suffix]
        # storing words that start sentences
        elif content[i - 1][-1] == "." or content[i - 1][-1] == "!" content[i - 1][-1] == "?":
            prefix = word + " " + content[i+1]
            chain["NONWORD"].append(prefix)
            suffix = content[i + 2] + " " + content[i + 3]
            if prefix in chain:
                chain[prefix].append(suffix)
            else:
                chain[prefix] = [suffix]
        # storing word that end sentences
        elif word[-1] == "." or word[-1] == "!" or word[-1] == "?":
            prefix = content[i - 1] + " " + word
            chain[prefix] = ["NONWORD"]
        else:
            prefix = word + " " + content[i+1]
            if content[i + 2][-1] == "." or content[i + 2][-1] == "!" or content[i + 2][-1] == "?":
                suffix = content[i + 2]
                chain[suffix] = ["NONWORD"]
            else:
                suffix = content[i + 2] + " " + content[i + 3]

            if prefix in chain:
                chain[prefix].append(suffix)
            else:
                chain[prefix] = [suffix]


    return chain


def build_sentence(chain):
    sentence = []
    word = random.choice(chain["NONWORD"])
    sentence.append(word)

    while chain[word] != ["NONWORD"]:
        word = random.choice(chain[word])
        sentence.append(word)


    sentence = ' '.join(sentence)
    return sentence


def get_sentence(full_text):
    chain = build_chain(full_text)
    markov_babel = build_sentence(chain)
    while len(markov_babel) > 280:
        markov_babel = build_sentence(chain)

    return markov_babel
