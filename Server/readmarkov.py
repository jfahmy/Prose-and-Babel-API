import random
import markovchain_pb2
import re

def generate_sentence(chain):
    sentence = []
    sources = []
    selected_word = random.choice(chain.link["NONWORD"].word)

    # print(selected_word.wordvalue)
    while selected_word.wordvalue != "NONWORD":
        sentence.append(selected_word.wordvalue)
        source = re.sub(r'@','#', selected_word.screen_name)
        sources.append(source)
        selected_word = random.choice(chain.link[selected_word.wordvalue].word)

    sentence = ' '.join(sentence)
    sources = ' '.join(sources)
    return [sentence, sources]


def get_markov():
    chain = markovchain_pb2.Chain()
    f = open("Prose-and-Babel-API/Server/celeb_chain.txt", "rb")
    chain.ParseFromString(f.read())
    print("!!!!!!!!!!!!READING CELEBRITY MARKOV")
    f.close()
    return chain
