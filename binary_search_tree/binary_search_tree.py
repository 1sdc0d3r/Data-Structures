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


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return f"Height: {self.height}"

    # def balance(self):
    #     if self.heightL == self.heightR:
    #         self.balanced = True
    #     else:
    #         self.balanced = False

    # Insert the given value into the tree
    def insert(self, value):
        node = BinarySearchTree(value)
        self.height += 1
        # * You don't need to check if empty because the tree will always be initializer with a single value
        # if not self.value:
        #     self.value = value
        # else:
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
        # self.balance()

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

    # Call the function `fn` on the value of each node use recursive or iterative
    # * pre-order traversal
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        orderedList = []
        def cb(x): return orderedList.append(x)
        node.for_each(cb)
        orderedList.sort()
        for num in orderedList:
            print(num)

    # Print the value of every node, starting with the given node, in an iterative breadth first traversal

    # ! BFT is like a queue
    def bft_print(self, node):
        # Create Queue
        # add root to queue
        queue = [node]
        # while queue is not empty
        while(queue):
            # node = pop head of queue
            node = queue.pop(0)
            # do the thing (print)
            print(node.value)
            # add children of node to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    #  Print the value of every node, starting with the given node, in an iterative depth first traversal

    # ! DFT is like a stack
    def dft_print(self, node):
        # Create stack
        # add root to stack
        stack = [node]
        # while stack is not empty
        while stack:
            # node = pop head of stack
            node = stack.pop()
            # do the thing (print)
            print(node.value)
            # add children of node to stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    #! Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
