#!/usr/bin/env python3

def swap_keys_values(s):
   d = {}
   for key in s:
      new_key = s[key]
      d[new_key] = key
   return d