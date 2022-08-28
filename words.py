import requests
import random

# Create words list form the below url

word_site = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(word_site)
WORDS_bytes = response.content.splitlines()
WORDS = []

for WORD in WORDS_bytes:
    decoded_word = WORD.decode('utf-8')
    WORDS.append(decoded_word)

random.shuffle(WORDS)
WORDS = WORDS[:151]

# print(WORDS)