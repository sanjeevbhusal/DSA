import typing
from typing import List, Any


class NoSuchElementException(Exception):
    pass


class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.first = None
        self.last = self.first
        self._size = 0

    def add_first(self, value: Any) -> None:
        # first create a node from the value passed.
        node = self.Node(value)
        # if the list is empty, set both "first" and "last" variable to new node,
        if self.is_empty():
            self.first, self.last = node, node
        else:  # if the list contains nodes, add the new node at beginning of list.
            node.next = self.first
            self.first = node

        self._size += 1

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def add_last(self, value: Any) -> None:
        # first create a node from the value passed
        node = self.Node(value)
        # if the list is empty, set both "first" and "last" variable to new node.
        if self.is_empty():
            self.first, self.last = node, node
        else:  # if the list contains nodes, add the new node at ending of list.
            self.last.next = node
            self.last = node

        self._size += 1

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def delete_first(self) -> None:
        # validate if the linked list contains any items
        if self.is_empty():
            raise NoSuchElementException()
        # if the list contains only 1 node, set both variable "first" and "last" to null
        if self.first == self.last:
            self.first, self.last = None, None
        else:  # delete the starting node from the list
            second = self.first.next
            self.first.next = None
            self.first = second

        self._size -= 1

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def delete_last(self) -> None:
        # validate if the linked list contains any items
        if self.is_empty():
            raise NoSuchElementException()
        # if the list contains only 1 node, set both variable "first" and "last" to null
        if self.first == self.last:
            self.first, self.last = None, None
        else:  # delete the last node from the list
            previous = self.get_previous(self.last)
            self.last = previous
            self.last.next = None

        self._size -= 1

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def index_of(self, value: Any) -> int:
        # iterate through all nodes of list and return the index of node(if found)
        current = self.first
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def contains(self, value: Any) -> bool:
        # iterate through all nodes of list and return if node exists or not.
        return self.index_of(value) != -1

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def reverse(self) -> None:
        # we need two variables in every loop. The second variable will point to the first variable
        if self.is_empty():
            return

        previous = self.first
        current = previous.next
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.last = self.first
        self.first = previous
        self.last.next = None

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def get_kth_from_end(self, position: int):
        # validate if the list is empty or position specified is more than total items in the list
        if self.is_empty() or position > self.size():
            raise NoSuchElementException()

        # first and second pointers should be "k - 1" nodes apart
        first, second = self.first, self.first
        distance_between_pointers = position - 1
        for i in range(distance_between_pointers):
            second = second.next

        # move both pointers forward until second pointer reaches the end.
        while second is not self.last:
            first = first.next
            second = second.next

        return first.value

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def get_middle(self) -> typing.Union[int, tuple]:
        # validate if the list is empty
        if self.is_empty():
            raise NoSuchElementException()

        # if b is "self.last", the list has odd elements. if b's next is none, the list has even
        first, second = self.first, self.first
        while second is not self.last and second.next is not self.last:
            second = second.next.next
            first = first.next

        if second is self.last:
            return first.value
        else:
            return first.value, first.next.value

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def has_loop(self) -> bool:
        # check if two pointers will be at same element. if yes, loop exists.
        first, second = self.first, self.first
        while second.next is not None:
            first = first.next
            second = second.next.next

            if first == second:
                return True
        return False

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def size(self) -> int:
        return self._size

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def to_array(self) -> List:
        values_list = []
        current_node = self.first
        while current_node is not None:
            values_list.append(current_node.value)
            current_node = current_node.next
        return values_list

        # Time Complexity: O(n)
        # Space Complexity: O(n)

    def is_empty(self: Any) -> bool:
        return self.first is None

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def get_previous(self, node: Node) -> typing.Union[Node, None]:
        current = self.first
        while current:
            if current.next is node:
                return current
            current = current.next

        return None

        # Time Complexity: O(n)
        # Space Complexity: O(1)

    def __repr__(self) -> str:
        return str(self.to_array())
