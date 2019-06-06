import turtle 


my_turtle = turtle.Turtle()
my_win = turtle.Screen()


def drawSpiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        drawSpiral(my_turtle, line_len-2)


def tree(my_turtle, branch_len):
    if branch_len > 0:
        my_turtle.forward(branch_len)
        my_turtle.right(20)
        tree(my_turtle, branch_len-5)
        my_turtle.left(40)
        tree(my_turtle, branch_len-5)
        my_turtle.right(20)
        my_turtle.backward(branch_len)

# my_turtle.left(90)
# drawSpiral(my_turtle, 200)
# tree(my_turtle, 50)
# my_win.exitonclick()


def hanoi(a,b,c,n):
    if n == 1:
        print(a+'--->'+c)
    else:
        hanoi(a,c,b,n-1)
        hanoi(a,b,c,1)
        hanoi(b,a,c,n-1)
        
hanoi('a','b','c',3)