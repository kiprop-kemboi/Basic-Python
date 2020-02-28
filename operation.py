task = int(input("choose the task\n\t1.multiplication\n\t2.subtraction\n\t3.addition\n\t4.division\n"))
x = int(input("enter a number\n"))
y = int(input("enter a number\n"))
z = int(input("enter a number\n"))
ans = 0
if(task == 1):
    print(x*y*z)
elif(task == 2):
    print(x-z-y)
elif(task == 3):
    print(x+y+z)
elif(task == 4):
    print(x/y/z)
else:
    print("output of the results\n\n")


task = str(input("choose the operation\n\tmultiplication\n\tdivision\n\taddition\n\tsubtraction\n"))
a = int(input("enter an integer\n"))
b = int(input("enter an integer\n"))
c = int(input("enter an integer\n"))
ans = 0
if(task == "multiplication"):
    print(a*b*c)
elif(task == "division"):
    print(a/b/c)
elif(task == "addition"):
    print(a+b+c)
elif(task == "subtraction"):
    print(a-b-c)
else:
    print("incorrect operation")