x = int(input("please enter your first number: "))
y = int(input("please enter your second number: "))
z = int(input("please enter your third number: "))

if x < y+z and y < x+z and z < x+y:
    print("It is a triangle")
else:
    print("It isn't a triangle.")

