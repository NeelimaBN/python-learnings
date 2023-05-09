"""
A simple module to store order assesment details
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

from typing import List
from .order import Order
from dataclasses import dataclass

@dataclass
class OrderAssesment:
    """This class calculates stats of orders"""
    def __init__(self,orderlist):
        self.orderList = orderlist        

    def order_price_list(self):
        orders_list = []
        for order_assesment in self.orderList:
            orders_list.append(order_assesment.order_price)
        return orders_list
    
    def avgerage(self) -> float:
        orders_list= self.order_price_list()
        return sum(orders_list)/len(orders_list)

    def minimum(self) -> int:
        return min(self.order_price_list())

    def maximum(self) -> float:
        return max(self.order_price_list())

    def standardDeviation(self) -> float:
        mean=self.avgerage()
        orders_list=self.order_price_list()
        orders_difference_sum=0.0
        for order in orders_list:
            orders_difference_sum=orders_difference_sum+((order-mean)**2)

        standardDeviation=((orders_difference_sum/len(orders_list))**0.5)
        
        return standardDeviation

    def distance_list(self):
        dist_list=[]
        for distance_assesment in self.orderList:
            dist_list.append(distance_assesment.customer.distance)
        return dist_list

    def avgerage_distance(self) -> float:
        dis_list= self.distance_list()
        return sum(dis_list)/len(dis_list)

    def minimum_distance(self) -> int:
        return min(self.distance_list())

    def maximum_distance(self) -> float:
        return max(self.distance_list())

    def standardDeviation_distance(self) -> float:
        mean=self.avgerage()
        dis_list=self.distance_list()
        orders_difference_sum=0.0
        for order in dis_list:
            orders_difference_sum=orders_difference_sum+((order-mean)**2)

        standardDeviation=((orders_difference_sum/len(dis_list))**0.5)
        
        return standardDeviation    




        

    
    

    
