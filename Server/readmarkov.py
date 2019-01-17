import random
import markovchain_pb2

def generate_sentence(chain):
    sentence = []
    source = []
    selected_word = random.choice(chain.link["NONWORD"].word)

    # print(selected_word.wordvalue)
    while selected_word.wordvalue != "NONWORD":
        sentence.append(selected_word.wordvalue)
        source.append(selected_word.screen_name)
        selected_word = random.choice(chain.link[selected_word.wordvalue].word)

    sentence = ' '.join(sentence)
    source = ' '.join(source)
    return [sentence, source]


def get_markov():
    chain = markovchain_pb2.Chain()
    f = open("Server/celeb_chain.txt", "rb")
    chain.ParseFromString(f.read())
    print("!!!!!!!!!!!!READING FILE")
    response = generate_sentence(chain)
    print(response)
    f.close()
    return response
