#!/usr/bin/python3
def print_last_digit(number):

  if number < 0:
    number = -1 * number
  new = number%10
  print(new, end ="")
  return(new)
