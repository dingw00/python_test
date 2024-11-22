
# from . import src1
import os
import sys

print("__name__:", __name__)
print("__package__:", __package__)
print("os.getcwd():", os.getcwd())
print(sys.path)

from src1 import hi_src1, test_src1


current_dir = os.path.dirname(__file__)
# os.chdir(current_dir)

print(os.getcwd(), "===============")
test_src1.func()

def change_hi():
    hi_src1.HI="yes"

if __name__ == "__main__":
    print(hi_src1.HI)
    change_hi()
    print(hi_src1.HI)