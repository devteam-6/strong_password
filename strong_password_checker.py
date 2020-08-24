#!/usr/bin/env python3

"""
Chapter 7 Excercise : Strong password Detection



"""
import re
__author__ = "Furichous Jones IV"
__version__ = "Fall 2020"


def main():
    """Launches the script."""
    print("Insert password")
    password = input()
    is_strong = check_password(password)

    password_state = 'strong' if is_strong else 'not strong' #ternary operator
    print("Your password is " + password_state)

def check_password(password):
    """
        Checks if the given passwod is strong.
        Arguments:
        password -- the specified password to check
    """
    is_strong = True
    lower_case = re.compile(r'[a-z]')
    upper_case = re.compile(r'[A-Z]')
    digit = re.compile(r'[0-9]')
    if len(password) < 8:
        is_strong = False
    if not lower_case.search(password):
        is_strong = False
    if not upper_case.search(password):
        is_strong = False
    if not digit.search(password):
        is_strong = False
    return is_strong

if __name__ == '__main__':
    main()
