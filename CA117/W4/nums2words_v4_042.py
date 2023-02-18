#!/usr/bin/env python3

import sys

def get_tens(n):
   tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
   if n >= 20:
      return tens[(n // 10) - 2] 
   else:
      return ""

def get_ones(n):
   ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
   if n < 20:
      return ones[n]
   elif n > 20 and n % 10 != 0:
      return ones[n % 10]
   else:
      return ""

num_words = {
   100: 'one hundred',
}
for i in range(0, 100):
   tens_word = get_tens(i)
   ones_word = get_ones(i)
   if tens_word == "":
      num_words[i] = ones_word
   elif ones_word == "":
      num_words[i] = tens_word
   else:
      num_words[i] = tens_word + "-" + ones_word

for line in sys.stdin:
   line = line.strip().split()
   out = [num_words[int(num)] for num in line]
   print(" ".join(out))
