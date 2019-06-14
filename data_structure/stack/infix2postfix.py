"""
中缀表示式转换为后缀表达式

需要一个存放操作符的栈op_stack，输出结果的列表output
步骤：
从左到右遍历表达式：
1. 若是数字，直接加入到output
2. 若是操作符，比较该操作符和op_stack中操作符的优先级，若优先级大于op_stack中的，则压入到op_stack中
    否则，将op_stack中优先级大于或等于该操作符优先级的所有操作符加入到output中，然后压入op_stack中
3. 若是左括号，压入到op_stack中
4. 若是右括号，将op_stack中所有左括号前面的操作符加入到output中
重复上面的步骤


后缀表达式求值

需要一个存放中间结果的栈num_stack
步骤：
从左到右遍历表达式：
1. 若是数字，压入到num_stack中
2. 若是操作符，取出num_stack中的前两个元素，第二个是表达式左边的操作数，计算表达式的值，将求值结果压入到num_stack中
"""


from linked_stack import LinkedStack


def infix2postfix(expression):
    output = []
    op_stack = LinkedStack()
    op_priority = {'*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '(': 0, ')': 0}

    for e in expression:
        if e == '(':
            op_stack.push(e)
        elif e == ')':
            while op_stack.first() != '(':
                output.append(op_stack.pop())
            op_stack.pop()
        elif e.isdigit():
            output.append(e)
        else:
            while not op_stack.is_empty() and op_priority[op_stack.first()] >= op_priority[e]:
                output.append(op_stack.pop())
            op_stack.push(e) 
    
    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return ''.join(output)


def postfix_eval(expression):
    num_stack = LinkedStack()

    for e in expression:
        if e.isdigit():
            num_stack.push(e)
        else:
            num1 = num_stack.pop()
            num2 = num_stack.pop()
            res = eval(num2 + e + num1)
            num_stack.push(str(res))

    return num_stack.pop()    


if __name__ == "__main__":
    print(infix2postfix('2+(3+5)*(6+4)*(8+3)'))
    print(postfix_eval('235+64+*83+*+'))