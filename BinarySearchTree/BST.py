class BinarySearchTree:

    # Initialize Binary Search Tree
    def __init__(self):
        # Leaves
        self.left = None
        self.right = None
        # Root
        self.data = None

    def append(self, data):
        # If Data of the node is None, set data right
        if self.data is None:
            self.data = data
            return self.data
        # If given data is less than the node data, do recursion in the right node
        elif data < self.data:
            self.left = BinarySearchTree() if self.left is None else self.left
            self.left.append(data)
        # Else given data is less than the node data, do recursion in the right node
        else:
            self.right = BinarySearchTree() if self.right is None else self.right
            self.right.append(data)

    def search(self, data):
        # If node data is the searching data return data
        if data == self.data:
            return self.data
        # If searching data is lower than the root data recurse left
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            return False
        # Else recurse right
        elif data >= self.data:
            if self.right:
                return self.right.search(data)
            return False
        else:
            return False

    def traverse_tree(self):
        # Element List
        lst = []
        # Check All Left Node Elements
        if self.left:
            lst += self.left.traverse_tree()
        # Check all Right Node Elements
        if self.right:
            lst += self.right.traverse_tree()

        lst.append(self.data)
        return lst

    def delete(self, data):
        # If Data is lower than node data -> GO TO LEFT NODES
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        # If data is greater or equal go right
        elif data >= self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # If Left and right is none return none
            if self.left is None and self.right is None:
                return None
            # If left none return right
            elif self.left is None:
                return self.right
            # If right none return left
            elif self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    # Finds Max Value
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # Finds Minimum Value
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def __repr__(self):
        return self.traverse_tree()

    def __str__(self):
        return f"{self.traverse_tree()}"
