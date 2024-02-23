#!/usr/bin/env python3
"""
atds.py
The module containing all of the data structures used in the
Advanced Topics in CS course at Poly.
"""
__author__ = "Richard White"
__version__ = "2024-02-13"


class Stack(object):
    """Describes a Stack that can be used with push
    and pop commands.
    """
    def __init__(self):
        self.st = []

    def push(self, item):
        self.st.append(item)

    def pop(self):
        if len(self.st) > 0:
            return self.st.pop()
        else:
            return None
    
    def peek(self):
        """Returns the item on the "top" of
        the list, as long as there's an item there.
        """
        if len(self.st) > 0:
            return self.st[-1]
        else:
            return None

    def size(self):
        return len(self.st)
    
    def is_empty(self):
        return len(self.st) == 0
    
    def __repr__(self):
        return str(self.st)
    
class Queue(object):
    """Describes a queue that can be used with enqueue
    and dequeue methods.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __repr__(self):
        return str(self.queue)
