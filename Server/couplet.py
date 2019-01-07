import markov
import pronouncing
import random

url = "http://www.gutenberg.org/cache/epub/996/pg996.html"

chain = markov.build_chain(url)

print(random.choice(list(chain)))
# pronouncing.rhymes("climbing")
