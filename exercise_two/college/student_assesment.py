"""
A simple module to store assesment details
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

import re
from .utils import patterns
from .student import Student
from dataclasses import dataclass

@dataclass
class StudentAssesment:
    """This class stores marks of a student"""
    student:Student
    subject:str
    marks:float

    def __post_init__(self):
        """This post init method checks validity of fields passed to constructor. """

        if not re.fullmatch(patterns.subject_pattern,self.subject):
            raise ValueError(patterns.subject_pattern_error)
        
        if isinstance(self.marks, str):
            try:
                self.marks=float(self.marks)
            except ValueError:
                raise ValueError('Marks has to be float or float string')
        elif not isinstance(self.marks, float):
            raise ValueError('Marks has to be float or float string')

        if self.marks<0.0 or self.marks>100.0:
            raise ValueError("marks has to be between 0 and 100")

    
        
    
