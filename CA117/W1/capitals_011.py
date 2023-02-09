#!/usr/bin/env python3

import sys

def uppercase(s):
   return s.upper()

for line in sys.stdin:
   line = line.strip()
   first = line[0]
   last = line[len(line) - 1]
   first = uppercase(first)
   last = uppercase(last)
   middle = line[1:len(line) - 1]
   word = first + middle + last
   print(word)
