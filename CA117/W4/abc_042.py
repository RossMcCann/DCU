#!/usr/bin/env python3

import sys

nums = sys.stdin.readline().split()
numsort = sorted(nums)

order = sys.stdin.readline().strip()
ordersort = sorted(order)

sorted_dic = dict(zip(ordersort, numsort))

ordered = [sorted_dic[char] for char in order]
print(" ".join(ordered))
