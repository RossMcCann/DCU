#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]

def all_vowels(s):
   s = s.lower()
   if 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s:
      return True

def iary_end(s):
   end = s[-4:]
   if end == 'iary':
      return True

def es(s, l):
   s = s.lower()
   if 'e' in s:
      return l.append(s)

e_words = []
for word in words:
   es(word, e_words)

most = 0
for word in e_words:
   word = word.lower().count('e')
   if word > most:
      most = word

print(f"Shortest word containing all vowels: {min((word for word in words if all_vowels(word)), key=len)}")
print(f"Words ending in iary: {len([word for word in words if iary_end(word)])}")
print(f"Words with most e's: {[word for word in e_words if word.lower().count('e') == most]}")
