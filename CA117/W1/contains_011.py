#!/usr/bin/env python3

import sys

def contains(left, right):
   for char in left:
      if char not in right:
         return False
      right = right.replace(char, "", 1)
   return True

for line in sys.stdin:
   line = line.strip().split()
   sub = line[0].upper()
   word = line[1].upper()

   print(contains(sub, word))
