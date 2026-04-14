"""
application entry point for the day2 project.
"""

import random


def generate_otp():
    """generate a 6-digit otp"""
    otp = random.randit(100000, 999999)
    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print(f"generated otp:{otp}")
