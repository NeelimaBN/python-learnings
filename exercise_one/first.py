#!/opt/homebrew/bin/python3
"""
A simple module template for Python
"""

__author__ = "Neelima Boppana <neelima_at_alvyl.com>"
__version__ = "0.1.0"
__license__ = "Proprietary"


def greet(user: str) -> None:
    """ Greet user """
    print("Hello, "+user)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    greet(123)