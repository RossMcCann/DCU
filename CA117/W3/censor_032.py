#!/usr/bin/env python3

import sys
args = sys.argv[1]

with open(args) as file:
   censors = [line.strip() for line in file]

lines = [line.strip() for line in sys.stdin]

for line in lines:
   for censor in censors:
      if censor in line:
         line = line.replace(censor, (len(censor) * '@'))
   print(line)