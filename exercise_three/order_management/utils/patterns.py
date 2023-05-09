"""
A simple module to write regular expressions for the customer and order details
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"

import re

#Regex for Student Name
name_pattern=re.compile(r'[a-zA-Z\.\ ]{3,22}')
name_pattern_error="Name should be alphabetical with spaces and period only and between 3 and 22 characters"

branch_pattern=re.compile(r'(CSE|ECE|EEE|IT)',re.IGNORECASE)
branch_pattern_error="Branch should be one of CSE,EEE,ECE,IT"

subject_pattern=re.compile(r'(UNIX|RDBMS|MATHS|MICROPROCESSORS|AI)',re.IGNORECASE)
subject_pattern_error="Subject should be UNIX,RDBMS,MATHS,MICROPROCESSORS,AI"

