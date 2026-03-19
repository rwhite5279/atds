#!usr/bin/env python3

"""
atds_tester.py
Runs a series of tests on the atds module, including looking at 
    * Stack
    * Queue
    * Deque
@author Richard White
"""


from atds import *

def main():

        print("Test passed: set_next() called") 
        tests_passed += 1
    except:
        print("Test failed: couldn't use set_next() method")

 

if __name__ == "__main__":
    main()
