#!/usr/bin/env python3

import sys

def quad_roots(a, b, c):
   a, b, c = int(a), int(b), int(c)

   sqr = (b ** 2) - (4 * a * c)
   if sqr < 0:
      return None
   else:
      pos_root = (-b + (sqr ** 0.5)) / (2 * a) 
      neg_root = (-b - (sqr ** 0.5)) / (2 * a)
      
      roots = [pos_root, neg_root]
      smallest, largest = min(roots), max(roots)

      return f'{smallest:.1f}, {largest:.1f}'

for line in sys.stdin:
   line = line.strip().split()
   n1, n2, n3 = line[0], line[1], line[2]
   print(quad_roots(n1, n2, n3))
