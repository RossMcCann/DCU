#!/usr/bin/env python3

import sys
lines = []

for line in sys.stdin:
   line = line.strip()
   lines.append(line)

longest = 0
for line in lines:
   if len(line) > longest:
      longest = len(line)

for line in lines:
   print(f"{line:^{longest}}")
