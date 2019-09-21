

n = int(input("Nhập số cạnh của đa giác:"))
m = ((n-2)*180)/n
a = 1
from turtle import *
shape("turtle")
color("red")
while a<=n:
    forward(100)
    left(180-m)
    a+=1
mainloop()
