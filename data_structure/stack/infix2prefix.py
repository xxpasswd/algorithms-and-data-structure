"""
中缀表达式转换为前缀表达式

需要两个栈，一个存放中间结果res_stack，一个存放操作符op_stack
步骤：
1. 从右向左遍历表达式：
    1.1 如果是操作数，将操作数压入到res_stack
    1.2. 如果是操作符，和op_stack中的元素比较优先级，若该操作符优先级大于op_stack中的元素，则压入op_stack中，
        否则将op_stack中优先级大于或等于目前元素优先级的所有操作符压入到res_stack中
    1.3 如果是右括号，将右括号压入到op_stack中
    1.4 如果是左括号，将op_stack中所有右括号前面的操作符压入到res_stack
    重复上面的步骤
2. 从res_stack中依次取出元素


前缀表达式求值

需要一个存放中间数的栈num_stack
步骤：
从右向左遍历式：
1. 如果是操作数，压入num_stack中
2. 如果是操作符，取出num_stack中的前两个元素，第一个元素的是表达左边的值，进行求值，然后将求值结果压入num_stack中
"""


from linked_stack import LinkedStack


def infix2prefix(expression):
    res_stack = LinkedStack()
    op_stack = LinkedStack()
    op_priority = {'*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '(': 0, ')': 0}

    width = 7 if len(expression) <=7 else len(expression)
    print(expression[::-1])
    print('Symbol'.center(8), 'op_stack'.center(width), 'res_stack'.center(width), sep = " | ")
    print('-'*(width*3+7))

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
            while op_stack.first() and op_priority[e] <= op_priority[op_stack.first()]:
                res_stack.push(op_stack.pop())
            op_stack.push(e)
        print_stack(e, op_stack, res_stack, width)

    while not op_stack.is_empty():
        res_stack.push(op_stack.pop())
    print_stack(' ', op_stack, res_stack, width)

    output = ''
    while not res_stack.is_empty():
        output += res_stack.pop()

    return output

def print_stack(e, op_stack, res_stack, width):
    print(e.center(8), str(op_stack).ljust(width), str(res_stack).ljust(width), sep=' | ')


def prefix_eval(expression):
    num_stack = LinkedStack()
    for e in reversed(expression):
        if e.isdigit():
            num_stack.push(e)
        else:
            num1 = num_stack.pop()
            num2 = num_stack.pop()
            res = eval(num1 + e + num2)
            num_stack.push(str(res))
    return num_stack.pop()


if __name__ == "__main__":
    print(infix2prefix('2+(3+5)*(6+4)*(8+3)'))
    print(prefix_eval('+2*+35*+64+83'))
