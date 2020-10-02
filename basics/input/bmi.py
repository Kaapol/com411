print("What is your name human?")
name = str(input())

print("How old are you?")
age = str(input())

print("How tall are you?")
height=float(input())

print("What is you weight in kg?")
weight =float(input())

bmi = weight / (height**2)

print("The bmi is {:.2f}.".format(bmi))

print(bmi)