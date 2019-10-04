number = (6, 7, 8, 90, 12, 78, 66)
n = int(input("Mời nhập số:"))

    
if n in number:
    print("Số có trong dãy.")
    print("Vị trí của số là:",number.index(n+1))
else:
    print("Số không có trong chuỗi.")