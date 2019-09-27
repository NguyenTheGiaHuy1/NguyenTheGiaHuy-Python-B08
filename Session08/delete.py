n = ['Toán', 'Công nghệ', 'Hóa', 'Văn']
n.append('Tin')
print(*n,sep=", ")
n.pop(1)
print(n)