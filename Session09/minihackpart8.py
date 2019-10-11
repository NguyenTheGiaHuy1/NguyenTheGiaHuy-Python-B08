diem = [45,60,50,100,75]
diem_moi = int(input("Nhập diểm mới của bạn:"))
diem.append(diem_moi)
for x,y in enumerate(diem):
    print(x+1,'.',y)

print("Sắp xếp lại:")
diem.sort(reverse=True)
for n,m in enumerate(diem):
    print(n+1, '.',m)

print("5 người có điểm cao nhất là :")
for a,s in enumerate(diem):
    if a+1<=5:
        print(a+1,'.',s)