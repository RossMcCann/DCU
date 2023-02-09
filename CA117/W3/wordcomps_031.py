#!/usr/bin/env python3

import sys

words = [s.strip() for s in sys.stdin]

def count_a(s):
   return s.lower().count('a')

def count_q(s):
   return s.lower().count('q')

def is_anagram(s):
   if s != 'angle':
      return sorted(s.lower()) == sorted("angle")


print(f'Words containing 17 letters: {[word for word in words if len(word) == 17]}')
print(f'Words containing 18+ letters: {[word for word in words if len(word) >= 18]}')
print(f"Words with 4 a's: {[word for word in words if count_a(word) == 4]}")
print(f"Words with 2+ q's: {[word for word in words if count_q(word) >= 2]}")
print(f'Words containing cie: {[word for word in words if "cie" in word]}')
print(f"Anagrams of angle: {[word for word in words if is_anagram(word)]}")
