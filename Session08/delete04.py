n = ['Toán', 'Công nghệ', 'Hóa', 'Văn']
n.append('Tin')
print(*n,sep=", ")

while True:
    m = str(input("Nhập vị trí cần bỏ:"))
    if m in n:
        n.remove(m)
        print(*n, sep= ", ")
        break
    else:
        print("Phần tử không tồn tại trong list. Yêu cầu kiểm tra lại.")