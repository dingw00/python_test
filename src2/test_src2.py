

import os
import sys

print("__name__:", __name__)
print("__package__:", __package__)
print("os.getcwd():", os.getcwd())

print(sys.path)


def func():
    print("A function from src2/test_src2.py")