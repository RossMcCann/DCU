#!/usr/bin/env python3

def get_divisors(n):
   nums = range(1, n + 1)
   divisors = sorted([i for i in nums if n / i == n // i])
   return divisors

def get_proper_divisors(n):
   nums = range(1, n)
   divisors = sorted([i for i in nums if n / i == n // i])
   return divisors

def is_perfect(n):
   proper_sum = sum(get_proper_divisors(n))
   return proper_sum == n
