#!/opt/homebrew/bin/python3
"""
A program to evaluate students marks
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

from college.student import Student
from college.student_assesment import StudentAssesment
from college.class_assesment import ClassAssesment

def create_data():
    s1=Student("Neelima",503,1,"A","CSE")
    s2=Student("Hari",504,1,"A","CSE")
    s3=Student("Sharma",505,1,"A","CSE")

    sa1=StudentAssesment(s1,'UNIX',65.0)
    sa2=StudentAssesment(s2,'UNIX',70.0)
    sa3=StudentAssesment(s3,'UNIX',90.0)

    global ca1

    ca1=ClassAssesment([sa1,sa2,sa3])

def process_data():

    global average_marks,min_marks,max_marks,standard_deviation

    average_marks=ca1.avgerage()
    min_marks=ca1.minimum()
    max_marks=ca1.maximum()
    standard_deviation=ca1.standardDeviation()

def output_information():
    
    print("The average of total Marks is : "+str(average_marks))
    print("The Minimum of total Marks is : "+str(min_marks))
    print("The Maximum of total Marks is : "+str(max_marks))
    print("The Standard Deviation of total marks is : "+str(standard_deviation))




if __name__ == "__main__":
    """ This is executed when run from the command line """
    create_data()
    process_data()
    output_information()