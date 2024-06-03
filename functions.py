def addNumbers(x):
    result = x + x
    return result
print(addNumbers(5))
print(addNumbers(4009))

def operatorsFunc(a,b):
    result = a * b
    return result 

print(operatorsFunc(4,9))

#call the function
print(operatorsFunc(900,40))
print(operatorsFunc(32,88))

y = 4
print(type(y))

g = True
print(type(g))

#convert float into integer
f = 9.5
print(int(f))

#convert integer to string
i = 20
print(str(i))

#string to integer
#string must be a number. cannot convert letters to number
z = "8"
print(int(z))

name = input("What's your name: ")
print("Your name is", name)

#multiple arguments
def multiplyFunc(c,d):
    multiply = c * d
    addition = c + d
    division = c/d
    subtraction = c-d
    return multiply, addition,division,subtraction
print(multiplyFunc(100,50))

#call the function
print(multiplyFunc(90,45))
print(multiplyFunc(70.5, 35.2))