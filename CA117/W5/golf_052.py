#!/usr/bin/env python3

import sys
playerscores = {}
disqualified = []

lines = sys.stdin.readlines()

for line in lines:
   try:
      line = line.strip().split()
      name = " ".join(line[:-3])
      score = int(line[-3]) + int(line[-2]) + int(line[-1])
      
      playerscores[name] = score
   
   # if an invalid score encountered add to disqualifed list
   except ValueError:
      disqualified.append(name)

# arrange by dictionary value lowest --> highest
scores = sorted(playerscores.items(), key=lambda item: item[1])
for score in scores:
   print(f'{score[0]}: {score[1]}')

disq = ", ".join(disqualified)
if disq != '':
   print(f'Disqualified: {disq}')
