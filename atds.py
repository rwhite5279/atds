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


class LinearSearcher(object):
    """Performs a linear search on a possible unorder list of numbers"""
    def search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return None

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
    def search(self, arr, value):
        if len(arr) == 0:
            return None
        middle = len(arr) //2
        if arr[middle] == value:
            return middle
        elif value < arr[middle]:
            return self.search(arr[:middle], value)
        else:
            return self.search(arr[middle + 1:], value)

class HashTable(object):
    def __init__(self, m):
        """Constructs parallel lists for our hash table"""
        self.m = m
        self.entries = 0
        self.keys = m * [None]
        self.values = m * [None]

    def hash_function(self, key, m):
        """Calculates a hashed index based
        on the modulo hash function"""
        return key % m

    def __len__(self):
        return self.entries

    def put(self, key, value):
        hash = self.hash_function(key, self.m) 
        while self.keys[hash] != None and self.keys[hash] != key: 
            hash = (hash + 1) % self.m
        if self.keys[hash] == None:
            self.entries += 1  # only increment for new entries
        self.keys[hash] = key
        self.values[hash] = value

    def get(self, key):
        hash = self.hash_function(key, self.m) 
        while self.keys[hash] != None and self.keys[hash] != key:
            hash = (hash + 1) % self.m
        return self.values[hash]

    def __repr__(self):
        return str(self.keys) + "\n" + str(self.values)
    
class BinaryTree(object):
    """Describes a BinaryTree, with a value and two children"""
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
    def get_root_val(self):
        return self.key
    def set_root_val(self, new_key):
        self.key = new_key
    def get_left_child(self):
        return self.left_child
    def get_right_child(self):
        return self.right_child
    def insert_left(self, key):
        new_binary_tree = BinaryTree(key)
        new_binary_tree.left_child = self.left_child
        self.left_child = new_binary_tree
    def insert_right(self,key):
        new_binary_tree = BinaryTree(key)
        new_binary_tree.right_child = self.right_child
        self.right_child = new_binary_tree
    def __str__(self):
        return "BinaryTree[key=" + str(self.key) \
               + ",left_child=" + str(self.left_child) \
               + ",right_child=" + str(self.right_child) + "]"

def main():
    print("Testing the binary_tree_class file!")
    bt = BinaryTree(3)
    print("Instruction: bt = BinaryTree(3)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=None,right_child=None]")
    print()
    bt.insert_left(4)
    print("Instruction: bt.insert_left(t4)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    bt.insert_left(5)
    print("Instruction: bt.insert_left(5)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=None]")
    print()
    bt.insert_right(6)
    print("Instruction: bt.insert_right(6)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=BinaryTree[key=6,left_child=None,right_child=None]]")
    print()
    bt.insert_right(7)
    print("Instruction: bt.insert_right(7)")
    print("Result:", bt) 
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=BinaryTree[key=7,left_child=None,right_child=BinaryTree[key=6,left_child=None,right_child=None]]]")
    print()
    l = bt.get_left_child()
    print("Instruction: l = bt.get_left_child()")
    print("Result: l =", l)
    print("Expect: l = BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    l.set_root_val(9)
    print("Instruction: l.set_root_val(9)")
    print("Result: l =", l)
    print("Expect: l = BinaryTree[key=9,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    l.insert_left(11)
    print("Instruction: l.insert_left(11)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=9,left_child=BinaryTree[key=11,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=None],right_child=BinaryTree[key=7,left_child=None,right_child=BinaryTree[key=6,left_child=None,right_child=None]]]")
    print()
    print("Instruction: print(bt.get_right_child().get_right_child())")
    print("Result:", bt.get_right_child().get_right_child())
    print("Expect: BinaryTree[key=6,left_child=None,right_child=None]")    
    
if __name__ == "__main__":
    main()


    
