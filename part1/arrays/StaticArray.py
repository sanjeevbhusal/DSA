class ArraySizeLimitReachedException(Exception):
    pass


class ArrayDoesnotContainAnyElementException(Exception):
    pass


class StaticArray:
    def __init__(self, size):
        self._array = [None] * size
        self._size = size  # it shows how many elements array can fit
        self._index = 0  # it is used to keep track of current index for pushing.

    def get(self, index):
        try:
            return self._array[index]
        except IndexError as e:
            raise e

    def push(self, item):
        if self._index == self._size:
            raise ArraySizeLimitReachedException("the arrays size has been reached.")

        self._array[self._index] = item
        self._index += 1

    def change(self, index, value):
        try:
            self._array[index] = value
        except IndexError as e:
            raise e

    @property
    def length(self):
        return self._size

    def __str__(self):
        return str(self._array)
