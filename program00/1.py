# Create list with inputs from user

list=[]
x=input("Enter number of numbers : ")

print(f"Input {x} numbers")

for i in range(0,int(x)):
    list.append(input())

print(f"Your list is {list}")
