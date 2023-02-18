#!/usr/bin/env python3

import sys

num_words = {
   0 : 'zero',
   1 : 'one',
   2 : 'two',
   3 : 'three',
   4 : 'four',
   5 : 'five',
   6 : 'six',
   7 : 'seven',
   8 : 'eight',
   9 : 'nine',
   10 : 'ten',
}

for line in sys.stdin:
   s = ''
   line = line.split()
   for num in line:
      num = int(num)
      if num in num_words:
         s = s + num_words[num] + ' '
      else:
         s = s + 'unknown' + ' '
   print(s[:-1])