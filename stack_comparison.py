#!/usr/bin/env python3
"""
stack_comparison.py
This program uses both a list-based Stack and an UnorderedList-based stack, and compares their 
performance on push() and pop() operations.
"""

__author__ = "Richard White"
__version__ = "2026-03-10"

import time
from atds import Stack, UnorderedListStack
import matplotlib.pyplot as plt
import numpy

def test_stack_pushes(s: Stack, n: int) -> float:
    """Pushes onto a stack n times and returns
    the amount of time in seconds that it took."""
    start = time.time()
    for i in range(n):
        s.push(i)
    stop = time.time()
    return stop - start
    
def test_uls_pushes(uls: UnorderedListStack, n: int) -> float:
    """Pushes onto a stack n times and returns
    the amount of time in seconds that it took."""
    start = time.time()
    for i in range(n):
        uls.push(i)
    stop = time.time()
    return stop - start

def test_stack_pops(s: Stack, n: int) -> float:
    """Pop from a stack n times and returns
    the amount of time in seconds that it took."""
    for i in range(n):
        s.push(i)
    start = time.time()
    for i in range(n):
        s.pop()
    stop = time.time()
    return stop - start

def test_uls_pops(uls: UnorderedListStack, n: int) -> float:
    """Pushes onto a stack n times and returns
    the amount of time in seconds that it took."""
    for i in range(n):
        uls.push(i)
    start = time.time()
    for i in range(n):
        uls.pop()
    stop = time.time()
    return stop - start

def main():
    # call the tests
    MIN_SIZE = 10000
    MAX_SIZE = 110000
    STEP = (MAX_SIZE - MIN_SIZE) // 10

    ################ Test 1. ############

    print("Testing Stack pushes...")
    size_list = [] # x-axis
    time_list = [] # y-axis
    for test_size in range(MIN_SIZE, MAX_SIZE, STEP):
        s = Stack()             # Create a new empty stack
        time_list.append(test_stack_pushes(s, test_size))
        size_list.append(test_size)

    # Now that the tests are done, create the plot (red dots)
    plt.plot(size_list, time_list, 'ro')
    # Create title, ylabel, and xlabel just once
    plt.title('Running time for Stacks vs number of push/pops')
    plt.ylabel('Time (s)')
    plt.xlabel('Number of pushes/pops')

    # identify linear best fit line for data
    # Create numpy arrays of x and y values (
    sizes = numpy.array(size_list)  # x-axis
    times = numpy.array(time_list)  # y-axis
    # Gets coefficients of polynomial 
    # For first-order polynomial here, just two coefficients:
    # m and b, for y = mx + b
    coefficients = numpy.polyfit(sizes, times, 1)
    # numpy generates a series of y values for the best fit line
    y_fit = numpy.polyval(coefficients, sizes)
    # Create label for trendline; `*coefficients` expands the tuple for formatting
    fit_label = 'List Stack push: y = {0:.8f}x + {1:.8f}'.format(*coefficients)
    plt.plot(sizes, y_fit, color='red', linestyle='-', label=fit_label)
    plt.legend(loc='upper left')

    ################ Test 2. ############

    print("Testing UnorderedListStack pushes...")
    size_list = [] # x-axis
    time_list = [] # y-axis
    for test_size in range(MIN_SIZE, MAX_SIZE, STEP):
        uls = UnorderedListStack()
        time_list.append(test_uls_pushes(uls, test_size))
        size_list.append(test_size)
    plt.plot(size_list, time_list, 'bo')

    # identify slope, intercept of linear best fit line for data
    times = numpy.array(time_list)
    sizes = numpy.array(size_list)
    coefficients = numpy.polyfit(sizes, times, 1)
    y_fit = numpy.polyval(coefficients, sizes)

    # Create label for trendline
    fit_label = 'Node Stack push: y = {0:.8f}x + {1:.8f}'.format(*coefficients)
    plt.plot(sizes, y_fit, color = 'blue', label=fit_label)
    plt.legend(loc='upper left')

    ################ Test 3. ############

    print("Testing Stack pops...")
    size_list = [] # x-axis
    time_list = [] # y-axis
    for test_size in range(MIN_SIZE, MAX_SIZE, STEP):
        s = Stack()
        time_list.append(test_stack_pops(s, test_size))
        size_list.append(test_size)
    plt.plot(size_list, time_list, 'go')

    # identify slope, intercept of linear best fit line for data
    times = numpy.array(time_list)
    sizes = numpy.array(size_list)
    coefficients = numpy.polyfit(sizes, times, 1)
    y_fit = numpy.polyval(coefficients, sizes)

    # Create label for trendline
    fit_label = 'List Stack pop: y = {0:.8f}x + {1:.8f}'.format(*coefficients)
    plt.plot(sizes, y_fit, color='green', linestyle='-', label=fit_label)
    plt.legend(loc='upper left')

    ################ Test 4. ############
    
    print("Testing UnorderedListStack pops...")
    size_list = [] # x-axis
    time_list = [] # y-axis
    for test_size in range(MIN_SIZE, MAX_SIZE, STEP):
        uls = UnorderedListStack()
        time_list.append(test_uls_pops(uls, test_size))
        size_list.append(test_size)
    plt.plot(size_list, time_list, 'mo')

    # identify slope, intercept of linear best fit line for data
    times = numpy.array(time_list)
    sizes = numpy.array(size_list)
    coefficients = numpy.polyfit(sizes, times, 1)
    y_fit = numpy.polyval(coefficients, sizes)

    fit_label = 'Node Stack pop: y = {0:.8f}x + {1:.8f}'.format(*coefficients)
    plt.plot(sizes, y_fit, color = 'magenta', linestyle='-', label=fit_label)
    plt.legend(loc='upper left')

    # Don't forget to show it all!
    plt.show()    


if __name__ == "__main__":
    main()
