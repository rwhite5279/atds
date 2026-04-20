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
        h.put(10, "f")
        h.put(12, "b")
        h.put(23, "c")
        tests_passed += 1
        print("SUCCESS. .put() method called with 5 values.")
    except:
        print("FAIL. Problem with .put() method.")

    print("\nTEST: Trying to print the current state of table...")
    try:
        print(h)
        print("Should look something like:")
        print("Keys:   [None, 1, 12, 23, None, None, 6, None, None, None, 10]")
        print("Values: [None, 'a', 'b', 'c', None, None, 'e', None, None, None, 'f']")
        tests_passed += 1
    except:
        print("FAIL. Couldn't print using __str__ or __repr__")

    print("\nTEST: Using put() for a function at the end of the table to see if it wraps around...")
    try:
        h.put(21, "g")
        if h.get(21) == "g":
            print("SUCCESS. .put() correctly wrapped in the table.")
            tests_passed += 1
        else:
            print("FAIL. .put() wraparound didn't work.")
        print(h)
    except:
        print("FAIL. .put() didn't correctly wrap the table in linear probe.")

    print("\nTEST: Checking the number of values in the hash table...")
    try:
        l = len(h)
        if l == 6:
            print("SUCCESS. len(h) is 6.")
            tests_passed += 1
        else:
            print("FAIL. len(h) should have been 5 -- solution is to write a __len__ method.")
    except:
        print("FAIL. Problem with len() method.")

    print("\nTEST: Looking for original hash in table...")
    try:
        result = h.get(10)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "f":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Replacing original hash {1, 'a'} in table with {1, 'z'}...")
    try:
        h.put(1, "z")
        result = h.get(1)
        if result == "z":
            print("SUCCESS. New value put and found.")
            tests_passed += 1
        else:
            print("FAIL. New value not put/found.")
    except:
        print("FAIL. Problem with replacing an old key.")

    print("\nTEST: Looking for key-collision in table...")
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
        print("FAIL. Problem with .get() finding a key-collision.")

    print("\nTEST: Looking for a hash that's not in table..")
    try:
        result = h.get(14)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent value not found.")
        else:
            print("FAIL. Non-existent value found.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for collision not in table...")
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
    print(tests_passed,"/ 12 tests passed")


if __name__ == "__main__":
    main()
