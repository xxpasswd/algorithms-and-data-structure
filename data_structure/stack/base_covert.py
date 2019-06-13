"""
10进制转换为其他进制:
通过短除法求进制
"""


from linked_stack import LinkedStack


def base_convert(num, base):
    base_str = '0123456789ABCEDF'
    stack = LinkedStack()
    
    while num:
        rem = num % base
        stack.push(rem)
        num = num // base

    output = ''
    while not stack.is_empty():
        output += base_str[stack.pop()]

    return output


if __name__ == "__main__":
    print(base_convert(5, 2))
    print(base_convert(15, 16))