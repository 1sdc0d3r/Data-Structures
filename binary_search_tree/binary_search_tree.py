"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    def insert(self, value):
        node = BinarySearchTree(value)
        if not self.value:
            self.value = value
        else:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = node
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value and self.left:
                self.left.contains(target)
            elif self.right:
                self.right.contains(target)
            else:
                return False

    """
    if there is right:
        get max on right
    else:
        return value
    """
    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

            # Print all the values in order from low to high
            # ? Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        orderedList = []
        def cb(x): return orderedList.append(x)
        node.for_each(cb)
        orderedList.sort()
        for num in orderedList:
            print(num)

    # ? Print the value of every node, starting with the given node, in an iterative breadth first traversal
    # todo
    def bft_print(self, node):
        orderedSet = set()
        def cb(x): return orderedSet.add(x)
        node.for_each(cb)
        orderedSet = sorted(orderedSet)
        return orderedSet
        # for num in orderedSet:
        #     print(num)

    # ? Print the value of every node, starting with the given node, in an iterative depth first traversal
    def dft_print(self, node):
        orderedList = []
        def cb(x): return orderedList.append(x)
        node.for_each(cb)
        for num in orderedList:
            print(num)

    #! Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
