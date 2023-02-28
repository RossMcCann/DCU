#!/usr/bin/env python3

import sys

for line in sys.stdin:
   nums = [num for num in line.strip().split()]
   unique_nums = [int(num) for num in nums if nums.count(num) == 1]
   if len(unique_nums) > 0:
      print(max(unique_nums))
   else:
      print('none')
