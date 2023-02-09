#!/usr/bin/env python3

import sys

def is_prime(n):
   for i in range(2, n // 2 + 1):
      if n % i == 0:
         return False
   return True

for line in sys.stdin:
   n = int(line.strip())
   nums = range(2, n + 1)

   print(f'Primes: {[n for n in nums if is_prime(n) == True]}')