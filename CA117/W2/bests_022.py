#!/usr/bin/env python3

import sys
args = sys.argv[1]
scores = {}
best = []

try:
   with open(args) as file:
      results = file.readlines()

      highest_grade = 0
      for line in results:
         try:
            line = line.strip().split()
            score = line[0]
            name = " ".join(line[1:])
            scores[name] = int(score)

            if int(score) > highest_grade:
               highest_grade = int(score)
               best_student = name

         except ValueError:
            print(f'Invalid mark {score} encountered. Skipping')

      for name in scores:
         if scores[name] == highest_grade:
            best.append(name)
      print(f'Best student(s): {", ".join(best)}')
      print(f'Best mark: {highest_grade}')

except FileNotFoundError:
   print(f'The file {args} could not be opened.')