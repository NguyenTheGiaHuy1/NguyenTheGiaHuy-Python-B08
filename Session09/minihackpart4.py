number = [6, 7, 8, 90, 12, 78, 66]
for i in number:
    if i%2==0:
        print(i)

numbers = input("Nhập dãy số:")
n = numbers.split(",")
for a in n:
    if int(a)%2==0:
        print(a)


        