"""
汉诺塔问题

思路：
使用递归解决
1.当总共有个n个盘子在a柱子上，假设我们已有方法将n个盘子移到c柱子上
2.当有n+1个盘子时，我们首先将n个盘子移到b柱子上
3.将第n+1个盘子移到c柱子上
4.再用同样的方法将n个盘子从b柱子上移到c柱子上
"""

def hanoi(n,a,b,c):
	if n==1:
		print("{}--->{}".format(a,c))
	else:
		hanoi(n-1,a,c,b)
		hanoi(1,a,b,c)
		hanoi(n-1,b,a,c)

if __name__ == '__main__':
	hanoi(3,'a','b','c')