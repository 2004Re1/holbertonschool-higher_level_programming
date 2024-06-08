#!/usr/bin/python3
"""JSON serialization of a Student object"""

class Student:
    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if attrs is None:
            return self.__dict__
        
        if not isinstance(attrs, list):
            return self.__dict__
        
        for item in attrs:
            if not isinstance(item, str):
                return self.__dict__
        
        return {key: value for key, value in self.__dict__.items() if key in attrs
