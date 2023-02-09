#!/usr/bin/env python3

import sys

def chop(s):
   return s[1: len(s) - 1]

for line in sys.stdin:
   line = line.strip()
   chopped = chop(line)
   if len(chopped) > 0:
      print(chopped)
