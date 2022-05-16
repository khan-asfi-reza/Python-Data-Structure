from typing import Generic, TypeVar

T = TypeVar("T")


class BinaryHeap(Generic[T]):
    __heap = []
    __length = 0

    def swap(self, left, right):
        self.__heap[left], self.__heap[right] = self.__heap[right], self.__heap[left]

    def heapify(self, index: int):
        largest: int = index
        # Left, Right Pointer
        left: int = 2 * index + 1
        right: int = 2 * index + 2
        # Logic Check
        if left < self.__length and self.__heap[left] > self.__heap[index]:
            largest = left
        if right < self.__length and self.__heap[right] > self.__heap[largest]:
            largest = right
        if largest != index:
            self.swap(largest, index)
            self.heapify(largest)

    def insert(self, element: T) -> None:
        # Append Data
        self.__heap.append(element)
        self.__length += 1
        # Length 0, Return None
        if self.__length == 0:
            return
        for i in range((self.__length // 2) - 1, -1, -1):
            self.heapify(i)

    def delete(self, element: T):
        i = 0
        for i in range(0, self.__length):
            if element == self.__heap[i]:
                break
        self.swap(i, self.__length - 1)
        self.__length -= 1
        for i in range((self.__length // 2) - 1, -1, -1):
            self.heapify(i)


