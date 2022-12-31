import os
import time

x = int(input("Enter the first number: "))
y = int(input("the second number: "))

print("Choose the operation you wanna use \n (1) ADD \n (2) SUBTRACT \n (3) MULTIPLY \n (4) DIVIDE \n (5) find other 3d shape values")


operation = int(input("Enter the number of which the option you wanna use: "))
if operation == 1:
    Sum = x + y
    print(Sum)
elif operation == 2:
    subtract = x - y
    print(subtract)
elif operation == 3:
    product = x * y
    print(product)
elif operation == 4:
    divide = x/y
    print(divide)
elif operation == 5:
    print("You want to Do some 3d solving eh :) \n\n\n")
    time.sleep(2)   
    os.system('cls')
print("(1) Cuboid \n (2) cylinder \n (3) cone \n (4) cube \n (5)sphere \n (6) Hemisphere \n")

def figure(number):
    print("Enter the length breadth and height and radius if nothing leave")
    l = int(input("Enter the length of figure: "))
    b = int(input("Enter the breadth of figure: "))
    h = int(input("Enter the height of figure: "))
    r = int(input("Enter the radius of figure: "))

    if number == 1:
        print("options \n () LSA \n (2) CSA \n (3) Volume ")
       
        tsa_cuboid = 2(l*b + b*h + l*h)
        csa_cuboid = 2(l + b)h
        volume = l*b*h
        
        
    elif number == 2:
        print("options \n () LSA \n (2) CSA \n (3) Volume ")
    elif number == 3:
        print("options \n () LSA \n (2) CSA \n (3) Volume ")
    elif number == 4:
        print("options \n () LSA \n (2) CSA \n (3) Volume ")
    elif number == 5:
        print("options \n () LSA \n (2) CSA \n (3) Volume ")
        
    elif number == 6:
        print("options \n () LSA \n (2) CSA \n (3) Volume ")

figure(number=int(input("Enter the number you want: ")))

