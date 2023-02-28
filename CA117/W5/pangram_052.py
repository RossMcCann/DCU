#!/usr/bin/env python3

import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'

lines = sys.stdin.readlines()
for line in lines:
   line = line.strip().lower()
   
   # puts every letter in a dictionary and sets value to False
   alphabet_dic = dict.fromkeys(alphabet, False)

   # changes value of letters to True if in the dictionary
   for char in line:
      if char in alphabet_dic:
         alphabet_dic[char] = True

   # puts the missing letters in a string
   missing = "".join([key for key in alphabet_dic if alphabet_dic[key] == False])
   
   if missing == "":
      print('pangram')
   else:
      print(f'missing {missing}')