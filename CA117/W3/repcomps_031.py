#!/usr/bin/env python3

import sys

for line in sys.stdin:
   n = (int(line.strip()))
   nums = range(1, n + 1)

   print(f'Non-multiples of 3 replaced: {[n if n % 3 == 0 else 0 for n in nums]}')
