#!/usr/bin/env python3

import sys
args1 = sys.argv[1]
args2 = sys.argv[2]

with open(args1) as file1:
   file1 = file1.read().strip()

with open(args2) as file2:
   file2 = file2.read().strip()

nums1 = file1.split()
nums2 = file2.split()
i = 0
while i < len(nums1):
   print(nums1[i])
   print(nums2[i])
   i = i + 1