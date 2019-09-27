n = ['Toán', 'Công nghệ', 'Hóa', 'Văn']
n.append('Tin')
print(*n,sep=", ")
m = int(input("Nhập vị trí cần bỏ:"))
n.pop(m)
print(*n, sep=", ")

  