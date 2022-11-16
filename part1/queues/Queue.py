class Queue:
    def __init__(self, size):
        self.storage = ['_'] * size
        self.rear = 0
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.storage)

    def enqueue(self, item):
        if self.is_full():
            raise Exception("queue is full.")

        self.storage[self.rear] = item
        self.rear = (self.rear + 1) % len(self.storage)
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")

        element = self.storage[self.front]
        self.storage[self.front] = "_"
        self.front = (self.front + 1) % len(self.storage)
        self.count -= 1
        return element

    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty")

        element = self.storage[self.front]
        return element

    def reverse(self):
        items_list = ['_'] * self.count
        index = 0
        while not self.is_empty():
            items_list[index] = self.dequeue()
            index += 1

        for i in range(len(items_list) - 1, -1, -1):
            self.enqueue((items_list[i]))

    def __repr__(self):
        my_array = []
        for i in range(self.front, len(self.storage)):
            my_array.append(self.storage[i])
        for i in range(0, self.front):
            my_array.append(self.storage[i])

        return str(my_array)
