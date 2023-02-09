#!/usr/bin/env python3

import sys
inp = [word.strip() for word in sys.stdin]
words = ([word for word in inp if len(word) >= 5])
lower_words = [word.lower() for word in words]

def bin_search(s, list_sort):
   low = 0
   high = len(list_sort) - 1
   while low <= high:
      mid = (low + high) // 2

      if list_sort[mid].lower() < s:
         low = mid + 1
      elif list_sort[mid].lower() > s:
         high = mid - 1
      else:
         return True
   return False

print([word for word in words if bin_search(word[::-1].lower(), lower_words)])