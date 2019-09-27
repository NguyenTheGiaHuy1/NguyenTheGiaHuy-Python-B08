n = ['Toán', 'Công nghệ', 'Hóa', 'Văn']
n.append('Tin')
print(*n,sep=", ")
n[0] = 'Spider Man'
print(*n,sep= ", ")