#!/usr/bin/env python3

import sys

def uppercase(s):
   return s.upper()

for line in sys.stdin:
   words = line.split()
   sub = uppercase(words[0])
   word = uppercase(words[1])
   if sub in word:
      print(True)
   else:
      print(False)
