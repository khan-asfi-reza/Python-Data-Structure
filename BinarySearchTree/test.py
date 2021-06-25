from unittest import TestCase

from BinarySearchTree.BST import BinarySearchTree


class TestBST(TestCase):
    __l = [1, 2, 3, 4, 5, 6, 7]

    def test_bst(self):
        bst = BinarySearchTree()

        for i in self.__l:
            bst.append(i)
        lst = bst.traverse_tree()
        lst.sort()
        for k in range(len(self.__l)):
            self.assertEqual(lst[k], self.__l[k])

        self.assertEqual(bst.find_max(), max(self.__l))
        self.assertEqual(bst.find_min(), min(self.__l))
