#!/usr/bin/env python3

from os import strerror
from string import ascii_lowercase

letters = []

try:
  # ask the user for the input file's name
  file_name = input("Enter the file name: ")
  f = open(file_name, 'rt')

  # read the file (if possible) and count all the Latin letters (lowercase and uppercase treated equally)
  for c in f.read():
    c = c.lower()
    if c.isalpha():
      letters.append(c)
  f.close()

  # print a simple histogram in alphabetical order (only non-zero counts should be presented)
  for l in ascii_lowercase:
    count = letters.count(l)
    if count > 0:
      print(f'{l} -> {count}')
    
except IOError as e:
  print(strerror(e.errno))
except:
  print("An error occurred")

