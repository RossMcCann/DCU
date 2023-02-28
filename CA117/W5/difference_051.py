#!/usr/bin/env python3

import sys
line1 = sys.stdin.readline().strip()
list1 = [char for char in line1]
line2 = sys.stdin.readline().strip()
list2 = [char for char in line2]

compared = list(zip(list1, list2))

output = ["-" if pair[0] == pair[1] else "*" for pair in compared]
print(line1)
print(line2)
print("".join(output))
