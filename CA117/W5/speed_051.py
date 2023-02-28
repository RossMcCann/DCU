#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]
pretime, predist = [int(t) for t in lines[0].strip().split()]

speeds = []
for line in lines[1:]:
   currtime, currdist = [int(t) for t in line.strip().split()]
   speed = (currdist - predist) // (currtime - pretime)
   speeds.append(speed)

   pretime, predist = currtime, currdist

print(max(speeds))