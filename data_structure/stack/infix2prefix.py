"""
中缀表达式转换为前缀表达式

需要两个栈，一个存放中间结果res_stack，一个存放操作符op_stack
步骤：
1. 从右向左遍历表达式：
    1.1 如果是操作数，将操作数压入到res_stack
    1.2. 如果是操作符，和op_stack中的元素比较优先级，优先级大于或等于op_stack中的元素，则压入op_stack中，
        否则将op_stack中优先级大于目前元素优先级的所有操作符压入到res_stack中
    1.3 如果是右括号，将有括号压入到op_stack中
    1.4 如果是左括号，将op_stack中所有右括号前面的操作符压入到res_stack
    重复上面的步骤
2. 从res_stack中依次取出元素
"""


from linked_stack import LinkedStack


def infix2prefix(expression):
    res_stack = LinkedStack()
    op_stack = LinkedStack()
    op_priority = {'*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '(': 0, ')': 0}

    for e in reversed(expression):
        if e == ')':
            op_stack.push(e)
        
        elif e == '(':
            while op_stack.first() != ')':
                res_stack.push(op_stack.pop())
            op_stack.pop()
        
        elif e.isdigit():
            res_stack.push(e)

        else:
            while op_stack.first() and op_priority[e] < op_priority[op_stack.first()]:
                res_stack.push(op_stack.pop())
            op_stack.push(e)
    
    while not op_stack.is_empty():
        res_stack.push(op_stack.pop())

    output = ''
    while not res_stack.is_empty():
        output += res_stack.pop()

    return output


if __name__ == "__main__":
    print(infix2prefix('2+(3+5)*(6+4)*(8+3)'))