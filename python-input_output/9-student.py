#!/usr/bin/python3
"""json"""


class student:
  
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


  def class_to_json(self):
      """Initialize an empty dictionary"""
      j_dict = {}

      for attr, value in self.__dict__.items():
          if isinstance(value, (list, dict, str, int, bool)):
              j_dict[attr] = value

      return j_dict
