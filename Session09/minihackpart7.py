diem = [45,60,50,100,75]
diem_moi = int(input("Nhập diểm mới của bạn:"))
diem.append(diem_moi)
for x,y in enumerate(diem):
    print(x+1,'.',y)

