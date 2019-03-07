'''
栈
is_empty():O(1)
size():O(1)
push(item):O(1)
pop():O(1)
peek():O(1)
'''

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

"""
用栈解决
平衡的括号,算法复杂度O(n)
"""
def par_check(s):
    a = Stack()
    balance = True
    index = 0
    while index<len(s) and balance:
        if s[index] == '(':
            a.push('(')
        elif s[index] == ')':
            if a.is_empty():
                balance = False
            else:
                a.pop()
        index += 1

    if balance and a.is_empty():
        return True
    else:
        return False

# print(par_check('(())()(()'))
"""
用栈解决进制转换，算法复杂度O(n)
"""
def base_covert(d, base):
    base_digit = '0123456789ABCDEF'

    s = Stack()
    while d>0:
        rem = d % base
        s.push(rem)
        d = d // base
    res = ''
    while not s.is_empty():
        res = res + base_digit[s.pop()]
    return res

# print(base_covert(25,26))

"""
将中缀表达式转换为后缀表达式
"""
def infix_to_posix(expression):
    precendence = {'(':1, '+':2, '-':2, '*':3, '/': 3, ')': 4}
    operator = Stack()
    ouput = []
    expression = expression.split()
    for token in expression:
        if token not in precendence:
            ouput.append(token)
        elif token == '(':
            operator.push(token)
        elif token == ')':
            o = operator.pop()
            while o != '(':
                ouput.append(o)
                o = operator.pop()
        else:
            while not operator.is_empty() and precendence[operator.peek()] >= precendence[token]:
                ouput.append(operator.pop())
            else:
                operator.push(token)
    while not operator.is_empty():
        ouput.append(operator.pop())

    return ''.join(ouput)    

# print(infix_to_posix('( A + B ) * C - ( D - E ) * ( F + G )'))

def posix_eval(expression):
    expression = expression.split()
    s = Stack()
    for i in expression:
        if i not in ('+','-','*','/'):
            s.push(i)
        else:
            prev = s.pop()
            prev_prev = s.pop()
            res = eval(prev_prev + i + prev)
            s.push(str(res))

    return s.pop()

# print(posix_eval('1 2 3 + *'))

