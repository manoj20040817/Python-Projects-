"Swap the Two variables without and with temp "

"with temp value"

x = int(input("enter the value of x: "))
y = int(input("enter the value of y: "))
temp = x
x = y
y = temp
print(f"x = {x}  ")
print(f"y = {y}")




"without temp value "

x = int(input("enter the value of x: "))
y = int(input("enter the value of y: "))

x , y = y , x
print(f"x = {x} ")
print(f"y = {y} ")