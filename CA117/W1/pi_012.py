#!/usr/bin/env python3

import sys 
from math import pi

for line in sys.stdin:
   decimal = line.strip()

   print(f"{pi:.{decimal}f}")
