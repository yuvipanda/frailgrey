#   shaney.py              by Greg McFarlane
#                          some editing by Joe Strout
#
#   search for "Mark V.  Shaney" on the WWW for more info!

import sys
import random 
import string

def generate(text, count):
    words = text.split()
    
    end_sentence = []
    dict = {}
    prev1 = ''
    prev2 = ''
    for word in words:
      if prev1 != '' and prev2 != '':
        key = (prev2, prev1)
        if dict.has_key(key):
          dict[key].append(word)
        else:
          dict[key] = [word]
          if prev1[-1:] == '.':
            end_sentence.append(key)
      prev2 = prev1
      prev1 = word
    
    key = ()
    sentence = ""   
    while 1:
      if dict.has_key(key):
        word = random.choice(dict[key])
        sentence = sentence + word + ' '
        key = (key[1], word)
        if key in end_sentence:
          yield sentence
          sentence = ""
          count = count - 1
          if count <= 0:
              break
      else:
        key = random.choice(end_sentence)
