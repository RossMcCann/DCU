#!/usr/bin/env python3

import sys

nums = sys.stdin.readline().strip().split()
nums = sorted([int(n) for n in nums])
nums = [str(n) for n in nums]
letters = sys.stdin.readline().strip()

abc = {
   'A': nums[0],
   'B': nums[1],
   'C': nums[2],
}

output = ""
for letter in letters:
   if letter in abc:
      output = output + abc[letter] + " "

print(output[:-1])