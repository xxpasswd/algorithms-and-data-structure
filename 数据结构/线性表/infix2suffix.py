'''
一个中缀表达式转后缀表达式的脚本

如果标记是操作数，将其附加到输出列表的末尾。
如果标记是左括号，将其压到 opstack 上。
如果标记是右括号，则弹出 opstack，直到删除相应的左括号。将每个运算符附加到输出列表的末尾。
如果标记是运算符，*，/，+或 - ，将其压入 opstack。但是，首先删除已经在 opstack 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中。

'''

import string
from stack import Stack

def infix2suffix(expression):
    ex_list = list(expression)
    # 定义各个运算符的优先级
    perc = {'*':3,'/':3,'+':2,'-':2,'(':1}
    out = []
    # 运算符堆栈
    op_s = Stack()

    nums_list = string.ascii_letters + string.digits
    for i in ex_list:
        if i == ' ':
            continue
        elif i in nums_list:
            out.append(i)
        elif i == '(':
            op_s.push(i)
        elif i == ')':
            op = op_s.pop()
            while op != '(':
                out.append(op)
                op = op_s.pop()
        else:
            if not op_s.is_empty():
                pre_op = op_s.pop()
                while perc[pre_op] > perc[i]:
                    out.append(pre_op)
                    if op_s.is_empty():
                        break
                    else:
                        pre_op = op_s.pop()
                else:
                    op_s.push(pre_op)       
            op_s.push(i)
    while not op_s.is_empty():
        out.append(op_s.pop())
    
    return ''.join(out)

expression = '2+(3+5)*(6+4)*(8+3)'
# expression = '2+3+4'
print(infix2suffix(expression))
