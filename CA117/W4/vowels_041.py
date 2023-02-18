#!/usr/bin/env python3

import sys
import string
vowel_count = {
   'a' : 0,
   'e' : 0,
   'i' : 0,
   'o' : 0,
   'u' : 0,
}

lines = [line.strip().lower() for line in sys.stdin]

for line in lines:
   a_count = line.count('a')
   vowel_count['a'] = vowel_count['a'] + a_count
   e_count = line.count('e')
   vowel_count['e'] = vowel_count['e'] + e_count
   i_count = line.count('i')
   vowel_count['i'] = vowel_count['i'] + i_count
   o_count = line.count('o')
   vowel_count['o'] = vowel_count['o'] + o_count
   u_count = line.count('u')
   vowel_count['u'] = vowel_count['u'] + u_count

longest = 0
for key in vowel_count:
   number = str(vowel_count[key])
   if len(number) > longest:
      longest = len(number)

items = sorted(vowel_count.items(), key=lambda item: item[1])[::-1]
for item in items:
   print(f'{item[0]} : {item[1]:>{longest}d}')
