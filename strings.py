a = 5

"""

String Reviews

"""
c = "The answer is {}".format(a) # Formatting a string
d = f"The anser is {a}" # Another format


"""

User Inputs

"""


operation = int(input("choose the condition \n\t1.subtraction \n\t2.multiplication \n\t3.division\n\t4.power\n"))
a = int(input("enter the number\n"))
b = int(input("enter the number\n"))
ans = 0
if(operation == 1):
    ans=(a-b)
elif(operation == 2):
    ans=(a*b)
elif(operation ==3):
    ans=(a/b)
elif(operation == 4):
    ans=(a**b)
else:
    print ("invalid operation")



print(ans)


















