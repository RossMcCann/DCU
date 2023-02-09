#!/usr/bin/env python3

import sys

for password in sys.stdin:
   password = password.strip()

   chartype = {
   "upper": 0,
   "lower": 0,
   "digit": 0,
   "symbol": 0,
}

   for char in password:
      if char.isupper() == True:
         chartype["upper"] = 1
      elif char.islower() == True:
         chartype["lower"] = 1
      elif char.isnumeric() == True:
         chartype["digit"] = 1
      else:
         chartype["symbol"] = 1

   total = chartype["upper"] + chartype["lower"] + chartype["digit"] + chartype["symbol"]
   print(total)
