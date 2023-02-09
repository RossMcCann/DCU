#!/usr/bin/env python3

import sys

def sort(a, b):
   print(sorted(a) == sorted(b))
  
for line in sys.stdin:
   line = line.strip().split()
   left = line[0]
   right = line[1]

   sort(left, right)
