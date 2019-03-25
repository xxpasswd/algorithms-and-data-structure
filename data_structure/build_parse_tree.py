"""
将带括号的数学表达式表示为一个树结构

过程：
遇见数字，将当前的节点设置为数字，返回父节点
遇见符号，将当前的节点设置为符号，右边插入节点，返回右边节点
遇见括号，左边插入一个树，开始括号里面表达式的树建立
"""
from node_tree import BinaryTree, m_w

def bulid_parse_tree(alist):
    # 先构建一个空树
    stack = []
    t = BinaryTree(None)
    stack.append(t)
    cur_t = t
    for i in alist:
        if i == '(':
            cur_t.insert_left(None)
            stack.append(cur_t)
            cur_t = cur_t.left            
        elif str(i).isdigit():
            cur_t.root = i
            parent = stack.pop()
            cur_t = parent
        elif i in ('+', '-', '*', '/'):
            cur_t.root = i
            cur_t.insert_right(None)
            stack.append(cur_t)
            cur_t = cur_t.right
        else:
            cur_t = stack.pop()
    return t

def evaluate(t):
    """
    表达式的计算使用递归
    """
    if t.root in ('+', '-', '*', '/'):
        left = evaluate(t.left)
        right = evaluate(t.right)
        t.root = eval(str(left) + str(t.root) + str(right))
        return t.root
    else:
        return t.root


t = bulid_parse_tree(['(', '3', '+', '(', '4', '*', '5' ,')',')'])
t.display()
m_w.exitonclick()        
print(evaluate(t))
