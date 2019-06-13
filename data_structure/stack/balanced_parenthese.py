"""
检测括号是否成对

((()()))  True
((()(())  False
"""


from linked_stack import LinkedStack


def balanced_parenthese(parenthese):
    stack = LinkedStack()
    for p in parenthese:
        if p == '(':
            stack.push(p)
        else:
            if stack.is_empty():
                return False
            stack.pop()
    return True if stack.is_empty() else False


if __name__ == "__main__":
    print(balanced_parenthese('((()()))'))
    print(balanced_parenthese('((()(())'))