#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
  for i in a_dictionary:
    if i is not key:
      return a_dictionary
  del a_dictionary[key]
  return a_dictionary


