'''
求最长不重复子串的长度
比如 abcdadc  最长不重复为 abcd 长度为4

解决思路：
遍历字符串，记下不重复字符串的开始索引，若遇到重复的字符，开始索引重置为重复字符的下一个位置，继续遍历，取最大长度的字符串
'''


def longest_no_repeat(s):
    # 不重复字符串的最大长度
    maxlen = 0
    # 最大子串的开始索引
    maxlen_index = 0
    # 已出现的字符和其索引
    used_char = {}
    # 不重复字符串的开始索引
    start = 0
    
    # 自己定义的函数，用来比较长度和更新最大子串的开始索引
    def lenmax(maxlen,maxlen_index,start,i):
        if i-start+1 >= maxlen:
            return i-start+1,start
        else:
            return maxlen,maxlen_index

    for i,char in enumerate(s):
        # 如果字符已经出现过，则更新不重复字符串的开始索引为重复字符的下一个位置
        if char in used_char:
            start = used_char[char]+1
        # 没有重复出现的话，对比当前不重复字符串和目前已知不重复字符串的最大长度
        else:
            maxlen,maxlen_index = lenmax(maxlen,maxlen_index,start,i)
        # 每次都添加或更新已出现字符的索引
        used_char[char] = i
    return maxlen,s[maxlen_index:maxlen_index+maxlen]   
 

if __name__ == '__main__':
    s = 'abcaedcebba'
    print(longest_no_repeat(s))
