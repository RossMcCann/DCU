#!/usr/bin/env python3

import sys

for email in sys.stdin:
   email = email.strip()
   split = email.split(".")
   mail = split[1]
   i = 0
   while i < len(mail) and mail[i].isalpha():
      i = i + 1

   surname = mail[0:i]
   print(split[0].capitalize(), surname.capitalize())
