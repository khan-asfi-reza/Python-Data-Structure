from LinkedList.linkedlist import LinkedList, Node
import unittest


class TestLinkedList(unittest.TestCase):
    __list_value = [1, 2, 3, 4, 5, 6, 7]
    __reverse_value = [7, 6, 5, 4, 3, 2, 1]

    def get_list_value(self):
        return self.__list_value

    def get_reverse_value(self):
        return self.__reverse_value

    def linked_list(self):
        return LinkedList(*self.get_list_value())

    def test_head(self):
        self.assertEqual(self.get_list_value()[0], self.linked_list().head)

    def test_tail(self):
        self.assertEqual(self.get_list_value()[-1], self.linked_list().tail)

    def test_reverse_insert_remove(self):
        reversed_link_list = LinkedList(*self.get_list_value())
        reversed_link_list.reverse()
        reversed_list = self.get_reverse_value()
        reversed_list.insert(4, 5)
        reversed_link_list.insert(4, 5)
        reversed_list.pop(5)
        reversed_link_list.remove(5)
        self.assertEqual(reversed_link_list.to_list(), self.get_reverse_value())

    def test_length(self):
        self.assertEqual(len(self.get_list_value()), len(LinkedList(*self.get_reverse_value())))


if __name__ == '__main__':
    unittest.main()
