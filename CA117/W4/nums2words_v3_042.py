#!/usr/bin/env python3

import sys
args = sys.argv[1]

with open(args) as inp:
   inp = [line.split() for line in inp]

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

translations = {}
for line in inp:
   translations[line[0]] = line[1]

for line in sys.stdin:
   s = ''
   line = line.split()
   for num in line:
      num = int(num)
      if num_words[num] in translations:
         word = num_words[num]
         s = s + translations[word] + ' '
   print(s[:-1]) 
