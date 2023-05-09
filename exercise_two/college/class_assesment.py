"""
A simple module to store class assesment details
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

from typing import List
from .student_assesment import StudentAssesment
from dataclasses import dataclass

@dataclass
class ClassAssesment:
    """This class stores marks of all students in a class"""
    marksList:List[StudentAssesment]

    #def __post_init__(self):
        #marks=[student_assesment.marks for student_assesment in self.marksList]
    
    def marks(self):
        marks_list = []
        for student_assesment in self.marksList:
            marks_list.append(student_assesment.marks)
        return marks_list

    def avgerage(self) -> float:
        marks_list = self.marks()
        return sum(marks_list)/len(marks_list)

    def minimum(self) -> float:
        return min(self.marks())

    def maximum(self) -> float:
        return max(self.marks())

    def standardDeviation(self) -> float:
        mean=self.avgerage()
        marks_list=self.marks()
        marks_difference_sum=0.0
        for mark in marks_list:
            marks_difference_sum=marks_difference_sum+((mark-mean)**2)

        standardDeviation=((marks_difference_sum/len(marks_list))**0.5)
        
        return standardDeviation

        

    
    

    
