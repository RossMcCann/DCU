#!/usr/bin/env python3

import sys

args = sys.argv[1]
with open(args) as file:
   contacts = [contact.strip() for contact in file]

name_number = {}
for contact in contacts:
   sep = contact.split()
   name = sep[0]
   number = sep[1]
   name_number[name] = number

for name in sys.stdin:
   name = name.strip()
   if name in name_number:
      print(f'Name: {name}')
      print(f'Phone: {name_number[name]}')
   else:
      print(f'Name: {name}')
      print(f'No such contact')