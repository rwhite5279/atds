#!/usr/bin/env python3
"""
HashTableTester.py
This program imports the HashTester class and uses it to store a range 
of key-value pairs.
@author Richard White
@version 2017-04-04
"""

from atds import *

def main():
    tests_passed = 0
    print("\nTEST: Creating HashTable(11)...")
    try:
        h = HashTable(11)
        tests_passed += 1
        print("SUCCESS. Table created.")
    except:
        print("FAIL. Table not created.")

    print("\nTEST: Using put function to store key-value pairs in table...")
    try:
        h.put(1, "a")
        h.put(6, "e")
        h.put(9, "f")
        h.put(12, "b")
        h.put(23, "c")
        tests_passed += 1
        print("SUCCESS. .put() method called with 5 values.")
    except:
        print("FAIL. Problem with .put() method.")

    print("\nTEST: Trying to print the current state of table:")
    try:
        print(h)
        print("Should look something like:")
        print("Keys:   [None, 1, 12, 23, None, None, 6, None, None, 9, None]")
        print("Values: [None, 'a', 'b', 'c', None, None, 'e', None, None, 'f', None]")
        tests_passed += 1
    except:
        print("FAIL. Couldn't print using __str__ or __repr__")
        


    print("\nTEST: Looking for original hash in table..")
    try:
        result = h.get(9)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "f":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for collision in table..")
    try:
        result = h.get(23)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "c":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for original hash not in table..")
    try:
        result = h.get(14)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent value not found.")
        else:
            print("FAIL. Non-existent value found.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for collision not in table..")
    try:
        result = h.get(45)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent collision not found.")
        else:
            print("FAIL. Non-existent collision found.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nResults:")
    print(tests_passed,"/ 9 tests passed")


if __name__ == "__main__":
    main()
