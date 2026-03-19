#!/usr/bin/env python3
"""
atds.py
A collection of data types for the Advanced Topics class.
Currently includes the Stack, Queue, and Deque classes.
"""
__author__ = "Richard White"
__version__ = "2026-02-12"

class Stack():
    def __init__(self):
        """Create an empty stack (as a list)"""
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def peek(self):
        """Returns the result if one available, otherwise None"""
        if len(self.stack) > 0:
            return self.stack[-1]
    def pop(self):
        """Returns the result if one available, otherwise None"""
        if len(self.stack) > 0:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0
    def __repr__(self):
        return str(self.stack)
    
class Queue(object):
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return len(self.queue) == 0
    def __repr__(self):
        return str(self.queue)

class Deque(object):
    """Defines a deque with the head (front) at 0
    and the tail (rear) at -1.
    """
    def __init__(self):
        self.deque = []
    def add_front(self, item):
        self.deque.insert(0, item)
    def add_rear(self, item):
        self.deque.append(item)
    def peek_front(self):
        if len(self.deque) > 0:
            return self.deque[0]
    def peek_rear(self):
        if len(self.deque) > 0:
            return self.deque[-1]
    def remove_front(self):
        if len(self.deque) > 0:
            return self.deque.pop(0)
    def remove_rear(self):
        if len(self.deque) > 0:
            return self.deque.pop(-1)
    def size(self):
        return len(self.deque)
    def is_empty(self):
        return len(self.deque) == 0

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data = new_data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]" 

class UnorderedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def length(self):
        node_count = 0
        current = self.head
        while current != None:
            node_count += 1
            current = current.get_next()
        return node_count

    def is_empty(self):
        return self.head == None
    
    def remove(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                # Modifications for multiple deletions
                previous = current
                current = current.get_next()
                # return
            else:
                previous = current
                current = current.get_next()
        return # default
    
    def pop(self, n = -1):
        """Clunky implementation--clean this up!"""
        if n == -1:
            if self.head == None:
                return None         # can't pop from an empty UL
            previous = None
            current = self.head     # current is a legal Node
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            data = current.get_data()
            if previous == None:
                self.head = None
            else:
                previous.set_next(None)
            return data
        else:
            if self.head == None:
                return None
            previous = None
            current = self.head
            index = 0
            while index < n:
                previous = current
                current = current.get_next()
                index += 1
            data = current.get_data()
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            return data
                
    def search(self, item):
        """Returns True if item found on UnorderedList"""
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

    def append(self, item):
        """Adds an item to the end of the UL"""
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)

    def index(self, item):
        if self.head == None:
            return None
        else:
            current = self.head
            i = 0
            while current.get_data() != item:
                current = current.get_next()
                i += 1
            return i

    def insert(self, position, item):
        new_node = Node(item)
        index = 0
        current = self.head
        if position == 0:
            if self.head == None:
                self.head = new_node
            else:
                new_node.set_next(current)
                self.head = new_node
        else:
            while index < position - 1:
                current = current.get_next()
                index += 1
            new_node.set_next(current.get_next())
            current.set_next(new_node) 

    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result     

class UnorderedListStack(object):
    """A Stack, implemented using the UnorderedList class"""
    def __init__(self):
        self.ul = UnorderedList()
    def push(self, item):
        """Use add at the top of the list--faster!"""
        self.ul.add(item)
    def pop(self):
        return self.ul.pop(0)
    def peek(self):
        item = self.ul.pop(0)
        self.ul.add(item)
        return item
    def is_empty(self):
        return self.ul.is_empty()
    def length(self):
        return self.ul.length()

class BinarySearcher(object):
    """A utility class that performs a binary search"""
    def __init__(self):
        pass
    def search(self, arr : list, value : int) -> int:
        lower = 0
        higher = len(arr) - 1
        while lower <= higher:
            middle = (lower + higher) // 2
            if arr[middle] == value:
                return middle
            elif value < arr[middle]:
                higher = middle - 1
            else:
                lower = middle + 1
        return None

class BinarySearcherRecursive(object):
    """A utility class that performs a binary search"""
    def __init__(self):
        pass
    def search(self, arr: list, value: int, lower: int, upper: int) -> int:
        if lower > upper:
            return None
        else:
            middle = (lower + upper) // 2
            if arr[middle] == value:
                return middle
            elif value < arr[middle]:
                return self.search(arr, value, lower, middle - 1)
            else:
                return self.search(arr, value, middle + 1, upper)

def main():
    pass

if __name__ == "__main__":
    main()


    
