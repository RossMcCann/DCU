#!/usr/bin/env python3

import sys
x = sys.stdin.read().strip()

while int(x) > 9:
   nums = str(x)
   nums = nums.replace("0", "")

   numslist = [int(num) for num in nums]

   product = 1
   for n in numslist:
      product = product * n
   
   x = product

print(x)