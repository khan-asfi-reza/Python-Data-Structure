from unittest import TestCase
from Stack.stack import Stack


class TestStack(TestCase):

    def test_stack(self):
        stack = Stack()

        self.assertEqual(stack.isEmpty(), True)

        self.assertEqual(stack.getSize(), 0)

        stack.push(3)
        stack.push(4)

        self.assertEqual(stack.peek(), 4)

        stack.pop()

        self.assertEqual(stack.peek(), 3)
