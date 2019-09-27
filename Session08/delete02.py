n = ['Toán', 'Công nghệ', 'Văn']
n.append('Tin')
print(*n,sep=", ")
if 'Hóa' in n:
    n.remove('Hóa')
    print(n)
else:
    print("Phần tử không tồn tại, yêu cầu kiểm tra lại.")
