# Project-CalculatorInPython
import re                       # regEx library

print("A basic calculator")
run = True
prev = 0

def fun():
    global run
    global prev
    equation = ""
    if prev == 0:
        equation = input("Enter the numbers:")
    else:
        equation = input(str(prev))
    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-z,#$&()" "]',"", equation)
    if prev == 0:
        prev = eval(equation)    # use eval which is a built in function 
    else:
        prev = eval(str(prev) + equation)

while run:
    fun()

