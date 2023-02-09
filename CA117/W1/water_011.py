#!/usr/bin/env python3

import sys

water = sys.stdin.readline().strip().split()
buckets = sys.stdin.readline().strip().split()

for litres in water:
   litres = int(litres)

total = 0
for bucket in buckets:
   bucket = int(bucket)
   if litres - bucket >= 0:
      total = total + 1
      litres = litres - bucket
   else:
      litres = 0
      total = total + 0

print(total)
