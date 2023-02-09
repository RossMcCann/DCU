#!/usr/bin/env python3

import sys
import calendar

def find_day(y, m, d):
   return calendar.weekday(y, m, d)

monday = "You were born on a Monday and Monday's child is fair of face."
tuesday = "You were born on a Tuesday and Tuesday's child is full of grace."
wednesday = "You were born on a Wednesday and Wednesday's child is full of woe."
thursday = "You were born on a Thursday and Thursday's child has far to go."
friday = "You were born on a Friday and Friday's child is loving and giving."
saturday = "You were born on a Saturday and Saturday's child works hard for a living."
sunday = "You were born on a Sunday and Sunday's child is fair and wise and good in every way."

for line in sys.stdin:
   line = line.strip().split()
   day, month, year = int(line[0]), int(line[1]), int(line[2])
   
   week_day = find_day(year, month, day)
   if week_day == 0:
      print(monday)
   elif week_day == 1:
      print(tuesday)
   elif week_day == 2:
      print(wednesday)
   elif week_day == 3:
      print(thursday)
   elif week_day == 4:
      print(friday)
   elif week_day == 5:
      print(saturday)
   else:
      print(sunday)
