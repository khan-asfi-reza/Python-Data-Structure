from unittest import TestCase
from Queue.q import Q


class TestQueue(TestCase):

    def test_stack(self):
        q = Q()

        self.assertEqual(q.isEmpty(), True)

        self.assertEqual(q.size(), 0)

        q.enqueue(4)
        self.assertEqual(q.dequeue_item(), 4)

        q.enqueue(5)
        q.dequeue()

        self.assertEqual(q.dequeue_item(), 5)