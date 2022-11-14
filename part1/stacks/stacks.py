import typing


class Stack:
    def __init__(self, size):
        self.storage = [0] * size
        self.count = 0
        self._min = None

    def is_empty(self):
        return self.count == 0

    def _increase_size(self):
        new_storage = [0] * (len(self.storage) * 2)
        for index, item in enumerate(self.storage):
            new_storage[index] = item
        self.storage = new_storage

    def push(self, item):
        if len(self.storage) == self.count:
            raise OverflowError()

        self.storage[self.count] = item
        self.count += 1

        if self._min is None:
            self._min = item
        else:
            if item < self._min:
                self._min = item

    def peek(self):
        if self.is_empty():
            return IndexError

        item = self.storage[self.count - 1]
        return item

    def get_minimum(self) -> typing.Union[int, None]:
        if self.is_empty():
            return None

        minimum = self.storage[0]
        for index in range(1, self.count):
            item = self.storage[index]
            if item < minimum:
                minimum = item
        return minimum

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError()

        item = self.storage[self.count - 1]
        self.count -= 1

        if self._min == item:
            self._min = self.get_minimum()

        return item

    def __repr__(self):
        return str([self.storage[i] for i in range(self.count)])

    def min(self) -> int:
        return self._min


class TwoStack:
    def __init__(self, size=10):
        self.storage = [0] * size
        self.count1 = 0
        self.count2 = 0

    def is_empty_1(self):
        return self.count1 == 0

    def is_empty_2(self):
        return self.count2 == 0

    def _increase_size(self):
        new_storage = [0] * (len(self.storage) * 2)
        for index, item in enumerate(self.storage):
            new_storage[index] = item
        self.storage = new_storage

    def push1(self, item):
        if self.count1 + self.count2 == len(self.storage):
            raise OverflowError()

        self.storage[self.count1] = item
        self.count1 += 1

    def push2(self, item):
        if self.count1 + self.count2 == len(self.storage):
            raise OverflowError()

        self.storage[len(self.storage) - 1 - self.count2] = item
        self.count2 += 1

    def peek_1(self):
        if self.is_empty_1():
            raise IndexError

        item = self.storage[self.count1 - 1]
        return item

    def peek_2(self):
        if self.is_empty_2():
            raise IndexError

        item = self.storage[len(self.storage) - self.count2]
        return item

    def pop1(self):
        if self.is_empty_1():
            raise IndexError

        item = self.storage[self.count1 - 1]
        self.count1 -= 1
        return item

    def pop2(self):
        if self.is_empty_2():
            raise IndexError

        item = self.storage[len(self.storage) - self.count2]
        self.count2 -= 1
        return item

    def get_stack_1(self):
        return str([self.storage[i] for i in range(self.count1)])

    def get_stack_2(self):
        return str([self.storage[len(self.storage) - 1 - i] for i in range(self.count2)])
