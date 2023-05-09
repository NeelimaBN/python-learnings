"""
A simple module to represent students in college
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

import re
from .utils import patterns
from dataclasses import dataclass

@dataclass
class Student:
    """This class represents a student in an Engineering college"""
    name:str
    rollNo:str|int
    semester:str|int
    section:str
    branch:str

    def __post_init__(self):
        """This post init method checks validity of fields passed to constructor. """

        if not re.fullmatch(patterns.name_pattern,self.name):
            raise ValueError(patterns.name_pattern_error)

        if isinstance(self.rollNo, str):
            try:
                self.rollNo=int(self.rollNo)
            except ValueError:
                raise ValueError('Roll Number has to be integer or integer string')
        elif not isinstance(self.rollNo, int):
            raise ValueError('Roll Number has to be integer or integer string')
        

        if isinstance(self.semester, str):
            try:
                self.semester=int(self.semester)
            except ValueError:
                raise ValueError('Semester has to be integer or integer string')
        elif not isinstance(self.semester, int):
            raise ValueError('Semester has to be integer or integer string')
        
        if self.semester <= 0 or self.semester > 8:
            raise ValueError("Semester has to be between 1 and 8")

        if self.section!='A' and self.section!='B':
            raise ValueError("Section has to be A or B")

        if not re.fullmatch(patterns.branch_pattern,self.branch):
            raise ValueError(patterns.branch_pattern_error)

        

