#!/usr/bin/env python3

import sys

def check(a,b):
   if a == b:
      return True
   else:
      return False

for line in sys.stdin:
   line = line.strip().lower()
   
   for char in line:
      if char.isalnum() == False:
         line = line.replace(char, "")
   
   reverse = line[::-1]
   print(check(line, reverse))
