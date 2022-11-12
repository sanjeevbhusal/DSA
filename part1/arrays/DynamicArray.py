class DynamicArray:
    def __init__(self, size):
        self._array = [0] * size
        self._length = 0

    def max(self):
        # loop over all items of the array and return the largest one.
        largest = self._array[0]
        for i in range(1, self._length):
            if self._array[i] > largest:
                largest = self._array[i]

        return largest

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def intersect(self, array1):
        intersection = []
        # we have to loop over all elements of our array and check if they are present in 'array'.
        for item in self._array:
            # to check, we can use index_of method. If method returns -1, element is not present, else it is present.
            index = array1.index_of(item)
            if index != -1:
                intersection.append(item)
        return intersection

        # Time Complexity: O(n ^ m)
        # Space Complexity: O(n + m)

    def reverse(self):
        # create a new array that is a reversed version of the original array.
        reversed_array = [0] * self._length
        for i in range(self._length - 1, -1, -1):
            reversed_array[self._length - 1 - i] = self._array[i]
        return reversed_array

        # Time Complexity: O(n)
        # Space Complexity: O(n)

    def insert_at(self, index, item):
        # array's size will increase by 1.

        # validate the index and make sure it is within the range.
        if index < 0 or index > self._length:
            raise IndexError("index out of bound exception")
        elif index == self.length:
            self.insert(item)
            return

        # replace the index value but store it in a variable.
        previous_value = self._array[index]
        self._array[index] = item

        # loop from the next index and shift other elements to one step right
        for index in range(index + 1, self._length):
            current_value = self._array[index]
            self._array[index] = previous_value
            previous_value = current_value

        # add the last value by incrementing the array if needed.
        self.insert(previous_value)

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def insert(self, item):
        # if the array is full, resize the array
        if len(self._array) == self._length:
            # create a new array of twice the size.
            new_array = [0] * len(self._array) * 2
            # copy all the elements into new array
            for i in range(self._length):
                new_array[i] = self._array[i]
            # set '_array' to new array
            self._array = new_array

        # add the item at the end of the array
        self._array[self._length] = item
        self._length += 1

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def remove_at(self, index_to_remove):
        # validate the index and make sure it is within the range.
        if index_to_remove < 0 or index_to_remove >= self._length:
            raise IndexError("index out of bound exception")

        # shift the items to the left to fill the hole
        for i in range(index_to_remove, self._length - 1):
            self._array[i] = self._array[i + 1]

        self._length -= 1

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def index_of(self, item_to_find):
        # loop over all items of the array and find the requested item
        for index in range(self._length):
            if self._array[index] == item_to_find:
                return index
        # if item is not found, return -1
        return -1

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def print(self):
        for i in range(self._length):
            print(self._array[i])

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    @property
    def length(self):
        return self._length

    def __repr__(self):
        return str(self._array)
