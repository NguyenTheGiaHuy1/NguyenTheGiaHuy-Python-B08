n = int(input("Nhập tháng:"))
if n==1 or n==3 or n==5 or n==7 or n==8 or n==9 or n==11:
    print("Tháng có 31 ngày")
elif n==2 or n==4 or n==6 or n==10 or n==12:
    print("Tháng có 30 ngày")
else:
    print("Không có tháng này")