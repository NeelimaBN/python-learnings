#!/opt/homebrew/bin/python3
"""
A program to evaluate orders
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

import random
from order_management.customer  import Customer
from order_management.order import Order
from order_management.order_assesment import OrderAssesment

def create_data():

    c1=Customer("Neelima", "Fortune Heights", 9.0)
    c2=Customer("Ridhi","Siyara Lights",7.5)
    c3=Customer("Pallavi","Sristy Symphony",8.5)

    order_id = random.randint(1,100)
    o1=Order(order_id,c1,5,10,5,2023,100)

    order_id = random.randint(1,100)
    o2=Order(order_id,c2,15,9,5,2023,100)

    order_id = random.randint(1,100)
    o3=Order(order_id,c3,10,8,5,2023,100)

    global ca1

    ca1=OrderAssesment([o1, o2, o3])

def process_data():

    global average_order,min_order,max_order,standard_deviation,avg_distance,min_distance,max_distance,standard_deviation_distance

    average_order=ca1.avgerage()
    min_order=ca1.minimum()
    max_order=ca1.maximum()
    standard_deviation=ca1.standardDeviation()
    avg_distance=ca1.avgerage_distance()
    min_distance=ca1.minimum_distance()
    max_distance=ca1.maximum_distance()
    standard_deviation_distance=ca1.standardDeviation_distance()

def output_information():
    
    print("The average of total Order price is : ",average_order)
    print("The Minimum of total Order price is : ",min_order)
    print("The Maximum of total Order price is : ",max_order)
    print("The Standard Deviation of Order price is : ",standard_deviation)
    print("The average of total Distance is : ",avg_distance)
    print("The Minimum of total Distance is : ",min_distance)
    print("The Maximum of total Distance is : ",max_distance)
    print("The Standard Deviation of Distance is : ",standard_deviation_distance)




if __name__ == "__main__":
    """ This is executed when run from the command line """
    create_data()
    process_data()
    output_information()