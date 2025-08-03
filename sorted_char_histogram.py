#!/usr/bin/env python3

from os import strerror

try:
  # ask the user for the input file's name
  filename = input("Enter the file name: ")
  f = open(filename, 'rt')
  letters = {}

  # read the file (if possible) and count all the Latin letters (lowercase and uppercase treated equally)
  line = f.readline()

  while line:
    for c in line:
      c = c.lower()
      
      if c.isalpha():
        if c not in letters:
          letters[c] = 1
        else:
          letters[c] += 1
          
    line = f.readline()
  f.close()
  
  # print a simple histogram 
  # output histogram will be sorted based on the character's frequency (bigger counts first)
  sort = sorted(letters.items(), key=lambda item: item[1], reverse=True)

  for char, count in sort:
    print(f'{char} -> {count}')
  
  # histogram should be sent to a file with the same name as the input with suffix '.hist' (concatenated)
  filename = filename.split('.')[0]
  f = open(f'{filename}.hist', 'wt')

  for char, count in sort:
    f.write(f'{char} -> {count}\n')
  f.close()
  
except IOError as e:
  print("I/O Error:", e.strerror)
except:
  print("An error occurred")

