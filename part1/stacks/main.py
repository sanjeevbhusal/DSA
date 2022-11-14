from stacks import Stack, TwoStack
from typing import Union


class Expression:
    def __init__(self, text: str, size=5):
        if type(text) is not str:
            return
        self.text = text
        self.left_bracket = ['(', '{', '[', "<"]
        self.right_bracket = [')', '}', ']', ">"]
        self.stack = Stack(size)

    def is_left_bracket(self, bracket: str) -> bool:
        return bracket in self.left_bracket

    def is_right_bracket(self, bracket: str) -> bool:
        return bracket in self.right_bracket

    def brackets_match(self, left_bracket: str, right_bracket: str) -> bool:
        return self.left_bracket.index(left_bracket) == self.right_bracket.index(right_bracket)

    def balanced_expression(self) -> bool:
        for char in self.text:
            if self.is_left_bracket(char):
                self.stack.push(char)
            elif self.is_right_bracket(char):
                # compare this bracket with the top element of the stack. if they are not matching pair, return False
                if self.stack.is_empty():
                    return False

                top_bracket = self.stack.pop()
                match = self.brackets_match(top_bracket, char)
                if not match:
                    return False

        return self.stack.is_empty()

        # Time Complexity: O(n)
        # Space Complexity: O(n)

    def reverse(self) -> Union[str, None]:
        for char in self.text:
            self.stack.push(char)

        reversed_string = ''
        while self.stack.is_empty() is False:
            char = self.stack.pop()
            reversed_string += char

        return reversed_string

        # Time Complexity: O(n)
        # Space Complexity: O(n)
