#!/usr/bin/env python3

import sys
one_bar = 400

def daily_bars(c):
   if c == 0:
      return c
   if c <= one_bar and c != 0:
      return 1
   elif not c % one_bar:
      return c // one_bar
   else:
      return (c // one_bar) + 1

for line in sys.stdin:
   calories = int(line.strip())
   print(daily_bars(calories))
