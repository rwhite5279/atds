#!/usr/bin/env python3
"""
binary_search_tester.py
"""

from atds import BinarySearcher

def main():
    bs = BinarySearcher()
    tests = [
        # (array, value_to_search, expected_result)
        ([1, 2, 3, 4, 7, 9, 13, 14, 20], 7, 4),
        ([1, 2, 3, 4, 7, 9, 13, 14, 20], 1, 0),
        ([1, 2, 3, 4, 7, 9, 13, 14, 20], 20, 8),
        ([1, 2, 3, 4, 7, 9, 13, 14, 20], -2, None),
        ([1, 2, 3, 4, 7, 9, 13, 14, 20], 23, None),
        ([1, 2, 3, 4, 7, 9, 13, 14, 20], 10, None),
        ([4, 7, 9, 13, 14, 20], 9, 2),
        ([4, 7, 9, 13, 14, 20], 13, 3),
        ([4, 7, 9, 13, 14, 20], 20, 5),
        ([4, 7, 9, 13, 14, 20], 2, None),
        ([4, 7, 9, 13, 14, 20], 10, None),
        ([4, 7, 9, 13, 14, 20], 22, None),
    ]

    for arr, value, expected in tests:
        result = bs.search(arr, value)
        if result == expected:
            print(f"PASS: {value} in {arr} -> {result}")
        else:
            print(f"FAIL: {value} in {arr} -> got {result}, expected {expected}")


if __name__ == "__main__":
    main()