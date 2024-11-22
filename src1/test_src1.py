

import os
import sys
import pickle

print("__name__:", __name__)
print("__package__:", __package__)
print("os.getcwd():", os.getcwd())
current_dir = os.path.dirname(__file__)

# sys.path.append(os.getcwd())

print(sys.path)
# os.chdir(current_dir)

def func():
    a = "svezsvez"
    print("==================A function from src1/test_src1.py=================")
    with open("from_test_src1.pkl", "wb") as f:
        pickle.dump(a, f)