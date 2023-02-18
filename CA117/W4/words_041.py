#!/usr/bin/env python3

import sys
import string

totals = {}

words = sys.stdin.read().split()
for word in words:
   word = word.strip(string.punctuation).lower()
   
  if word not in totals:
      totals[word] = 1
   elif word in totals:
      totals[word] = totals[word] + 1

for key in sorted(totals):
   print(f'{key} : {totals[key]}')
