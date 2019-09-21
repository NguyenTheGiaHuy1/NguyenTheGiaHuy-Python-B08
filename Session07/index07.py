n = int(input("Nhập số:"))
m = n%2
if m == 1:
    print(n,"là số lẻ")
    b = 1
    while b<n+2:
        print(b)
        b+=2
else:
    print(n,"là số chẵn")
    c = 1
    while c<n:
        print(c)
        c+=2

    



