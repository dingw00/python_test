

import os
import sys

print("__name__:", __name__)
print("__package__:", __package__)
current_dir = os.path.dirname(__file__)

# Inside package, path from this package
# Need to add package path
sys.path.append(current_dir)
import src1_1
import test_src1

HI="hello"
# Outside package, path from root
# Add root path here
root_folder = current_dir[:current_dir.find("/test/")]+"/test"
sys.path.append(root_folder)
print(sys.path)

# os.chdir(current_dir)

from src2 import hi_src2
import __init__
print("========RUNNUNG hi_src1.py=========")
print("os.getcwd() =", os.getcwd())
print(__init__.HELLO)
if __name__ == "__main__":
    print("hi_src1, running main function")
    print(__init__.HELLO)
    test_src1.func()
