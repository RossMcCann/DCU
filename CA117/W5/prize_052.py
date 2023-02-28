#!/usr/bin/env python3

import sys

# start point and order in 2 seperate variables from stdin
start = sys.stdin.readline().strip()
order = sys.stdin.readline().strip()

# functions to move the 'cups' around
def a(p):
   tmp = p[0]
   p[0] = p[1]
   p[1] = tmp
   return p

def b(p):
   tmp = p[1]
   p[1] = p[2]
   p[2] = tmp
   return p

def c(p):
   tmp = p[0]
   p[0] = p[2]
   p[2] = tmp
   return p

# replace the start with a different element
cups = '123'
prize = cups.replace(start, 'p')
prizes = [n for n in prize]

# move the 'cups'
for char in order:
   if char == 'A':
      prizes = a(prizes)
   elif char == 'B':
      prizes = b(prizes)
   else:
      prizes = c(prizes)

# will be at the point +1 because of list indexing
print(prizes.index('p') + 1)
