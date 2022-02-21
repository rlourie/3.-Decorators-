from Decor import decor


class Stack:
    @decor('log.txt')
    def __init__(self):
        self.items = []

    @decor('log.txt')
    def is_empty(self):
        return self.items == []

    @decor('log.txt')
    def push(self, item):
        self.items.append(item)

    @decor('log.txt')
    def pop(self):
        return self.items.pop()

    @decor('log.txt')
    def peek(self):
        return self.items[-1]

    @decor('log.txt')
    def size(self):
        return len(self.items)


@decor('log.txt')
def reverse(open_bracket_func):
    if open_bracket_func == ')':
        return '('
    else:
        return chr(ord(open_bracket_func) - 2)


@decor('log.txt')
def checker(open_br, check_str):
    My_Stack = Stack()
    for bracket in check_str:
        if bracket in open_br:
            My_Stack.push(bracket)
        elif My_Stack.is_empty() == False and My_Stack.peek() == reverse(bracket):
            My_Stack.pop()
        else:
            print("No correct")
            return

    if My_Stack.is_empty():
        print("Correct")
    else:
        print("No correct")


if __name__ == '__main__':
    check = '[[{())}]'
    open_bracket = ['(', '{', '[']
    checker(open_bracket, check)
