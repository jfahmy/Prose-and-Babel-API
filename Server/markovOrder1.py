import random

def build_chain(full_text):
    chain = {}
    full_text = full_text.split()
    for i,word in enumerate(full_text):
        if i == len(full_text) - 1:
            chain[word] = ["NONWORD"]
            break
        elif i == 0:
            chain["NONWORD"] = [word]
            chain[word] = [full_text[i + 1]]
        # storing words that start sentences
        elif full_text[i - 1][-1] == "." or full_text[i - 1][-1] == "!" or full_text[i - 1][-1] == "?":
            chain["NONWORD"].append(word)
            if word in chain:
                chain[word].append(full_text[i + 1])
            else:
                chain[word] = [full_text[i + 1]]
        # storing words that end sentences
        elif word[-1] == "." or word[-1] == "!" or word[-1] == "?":
            chain[word] = ["NONWORD"]
        # storing everything else
        else:
            if word in chain:
                chain[word].append(full_text[i + 1])
            else:
                chain[word] = [full_text[i + 1]]

    return chain

def generate_sentence(full_text):
    chain = build_chain(full_text)
    sentence = []
    word = random.choice(chain["NONWORD"])
    sentence.append(word)

    while chain[word] != ["NONWORD"]:
        word = random.choice(chain[word])
        sentence.append(word)

    sentence = ' '.join(sentence)
    return sentence
