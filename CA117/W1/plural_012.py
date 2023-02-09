#!/usr/bin/env python3

import sys

vowels = "aeiou"
es_endings_double = "chsh"
es_endings_single = "xsz"
ves_ending = "fe"

for line in sys.stdin:
   line = line.strip()

   if line[-2:] in es_endings_double or line[-1:] in es_endings_single:
      line = line + "es"
   elif line[-2] not in vowels and line[-1] == "y":
      line = f"{line[0:-1]}ies"
   elif line[-2:] in ves_ending:
      line = f"{line[0:-2]}ves"
   elif line[-1] == "f":
      line = f"{line[0:-1]}ves"
   elif line[-1] == "o":
      line = line + "es"
   else:
      line = line + "s"

   print(line)
