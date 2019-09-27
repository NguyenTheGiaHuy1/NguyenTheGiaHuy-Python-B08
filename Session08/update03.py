n = ['Toán', 'Công nghệ', 'Hóa', 'Văn']
n.append('Tin')
print(*n,sep=", ")
a = int(input("Nhập vị trí cần sửa:"))
m = input("Nhập nội dung thay thế:")
n[a] = m
print(*n,sep = ", ")
