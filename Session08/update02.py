n = ['Toán', 'Công nghệ', 'Hóa', 'Văn']
n.append('Tin')
print(*n,sep=", ")
n[0] = 'Spider Man'
n[-1] = 'Harry Porter'

print(*n,sep= ", ")
