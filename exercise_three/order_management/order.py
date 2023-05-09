"""
A simple module to store order details
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

import re
import datetime
from .utils import patterns
from .customer import Customer
from dataclasses import dataclass

@dataclass
class Order:
    """This class stores order details of a order"""
    order_id:int
    customer:Customer
    quantity:int
    date:int
    month:int
    year:int
    order_price:int

    def __post_init__(self):
        """This post init method checks validity of fields passed to constructor. """
        
        if isinstance(self.quantity, str):
            try:
                self.quantity=int(self.quantity)
            except ValueError:
                raise ValueError('quantity has to be int or int string')
        elif not isinstance(self.quantity, int):
            raise ValueError('quantity has to be int or int string')

        if self.quantity<0 or self.quantity>10000:
            raise ValueError("quantity has to be between 0 and 10000")

        if isinstance(self.date, str):
            try:
                self.date=int(self.date)
            except ValueError:
                raise ValueError('Date has to be int or int string')
        elif not isinstance(self.date, int):
            raise ValueError('Date has to be int or int string')

        if self.date<0 or self.date>31:
            raise ValueError("Date has to be between 0 and 32")

        if isinstance(self.month, str):
            try:
                self.month=int(self.month)  
            except ValueError:
                raise ValueError('Month has to be int or int string')
        elif not isinstance(self.month, int):
            raise ValueError('Month has to be int or int string')
        
        if self.month<0 or self.month>12:
                    raise ValueError("Month has to be between 0 and 13")

        if isinstance(self.year, str):
            try:
                self.year=int(self.year)
            except ValueError:
                raise ValueError('year has to be int or int string')
        elif not isinstance(self.year, int):
            raise ValueError('year has to be int or int string')  

        if self.year<2023:
            raise ValueError("year has to be 2023")
     
        
        self.order_price=self.quantity*100
        
    
        
    
