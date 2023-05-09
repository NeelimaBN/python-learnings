"""
A simple module to represent customers for order management
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

import re
from .utils import patterns
from dataclasses import dataclass

# @dataclass
class Customer:
    """This class represents a customer """
    def __init__(self,name,address,distance):
        self.name = name
        self.address = address
        self.distance = distance
    

    def __post_init__(self):
        """This post init method checks validity of fields passed to constructor. """

        if not re.fullmatch(patterns.name_pattern,self.name):
            raise ValueError(patterns.name_pattern_error)

        if isinstance(self.distance, str):
            try:
                self.distance=float(self.distance)
            except ValueError:
                raise ValueError('distance has to be float or float string')

        elif not isinstance(self.distance, float):
            raise ValueError('Semester has to be float or float string')
        
        if self.distance <= 0 or self.distance > 10:
            raise ValueError("Distance has to be between 0 and 10 kms")

        

