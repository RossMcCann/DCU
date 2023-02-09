#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]

def qnou(s):
   s = s.lower()
   if 'qu' in s:
      s = s.replace('qu', '')

   if 'q' in s:
      return True
   else:
      return False


print(f'Words with q but no u: {[word for word in words if qnou(word)]}')
