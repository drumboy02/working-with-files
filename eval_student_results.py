#!/usr/bin/env python3

from os import strerror
# program should be protected against all possible failures. errors should be presented to the user
# - file doesn't exist
# - input data failures
# - data error should terminate the program

# implement exceptions hierarchy
class StudentsDataException(Exception):
  pass

class BadLine(StudentsDataException):
  # raised when a wrong line is detected
  def __init__(self, msg="A wrong line was detected"):
    super().__init__(self)
    self.msg = msg

class FileEmpty(StudentsDataException):
  # raised when the source file exists but is empty
  def __init__(self, msg="Source file is empty"):
    super().__init__(self)
    self.msg = msg

try:
  # ask the user for Prof. Jekyll's file name
  file_name = input("Enter the file name: ")
  
  # read the file contents and count the sum of the received points for each student
  students = {}
  
  with open(file_name, 'rt') as file:
    line = file.readline()
    
    if not file.tell():
      raise FileEmpty()
    
    while line:
      try:
        assert type(line[0]) == str
        assert type(line[9]) == str
        assert type(int(line[18])) == int
      except:
        raise BadLine()
      
      line = line.replace('\n', '').split()
      
      if len(line) != 3:
        raise Badline()
      
      fname, lname, score = line[0], line[1], line[2]
      
      student = f'{fname} {lname}'

      if student not in students:
        students[student] = float(score)
      else:
        students[student] += float(score)
      
      line = file.readline()
  
  # print a simple (sorted) report
  students = sorted(students.items())
  
  for student in students:
    full_name = student[0].split()
    score = student[1]
    print(f'{full_name[0]}\t {full_name[1]}\t {score}')
  
except IOError as e:
  print("An error occurred:", strerror(e.errno))
except BadLine as e:
  print("An error occurred:", e.msg)
except FileEmpty as e:
  print("An error occurred:", e.msg)

