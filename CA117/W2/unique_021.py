#!/usr/bin/env python3

import sys
import string

words = {}
def unique(s, d):
   if s != "":
      if s not in d:
         d[s] = 1
      else:
         d[s] = d[s] + 1

for line in sys.stdin:
   line = line.strip().lower().split()

   for word in line:
      word = word.strip(string.punctuation)
      unique(word, words)

print(len(words))
            