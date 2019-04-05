"""
This file was created for retrieving 20 Chuck Norris Jokes via API.
These 20 Jokes were splitted into its single word to finally get the 25 % most ocuring words.
"""


from urllib import request
import json
from collections import Counter
import numpy as np
import pandas as pd

# CONFIGURE CONSOLE PROPERTIES
DESIRED_WIDTH = 320
pd.set_option('display.width', DESIRED_WIDTH)
np.set_printoptions(linewidth=DESIRED_WIDTH)
pd.set_option('display.max_columns', 15)

JOKE_ARRAY = []

# RETRIEVE 20 CHUCK NORRIS JOKES VIA API
# EXTRACT ONLY THE JOKE FROM THE WHOLE DATA
# APPEND RAW JOKE TO NEW ARRAY
for x in range(20):

    url = "http://api.icndb.com/jokes/random/1"

    connection = request.urlopen(url)

    data = connection.read()
    jsonInhalt = data.decode('utf-8')

    jsonDict = json.loads(jsonInhalt)

    joke = jsonDict["value"][0]
    raw_joke = joke["joke"]
    JOKE_ARRAY.append(raw_joke)

MY_ARRAY = str(JOKE_ARRAY)

# DELETE UNNECESSARY CHARS FORM STRING
for char in '.,\n,"",;,:':
    MY_ARRAY = MY_ARRAY.replace(char, ' ')
MY_ARRAY = MY_ARRAY.lower()

MY_ARRAY = MY_ARRAY.replace("'", " ")

# DELETE MULTIPLE SPACES FROM STRING
for x in range(5):
    MY_ARRAY = MY_ARRAY.replace("  ", " ")

print(MY_ARRAY)

# SPLIT ARRAY IN SINGLE WORDS
WORD_ARRAY = MY_ARRAY.split()

# COUNTS THE NUMBER OF WORDS
ALL_WORDS = Counter(WORD_ARRAY).most_common()
print("ALL WORDS: \n")
print(ALL_WORDS)
print("25 PERCENT MOST FREQUENT WORDS: \n")
EXTRACTED_WORDS = ALL_WORDS[0:int(len(ALL_WORDS)*0.25)]
print(EXTRACTED_WORDS)
