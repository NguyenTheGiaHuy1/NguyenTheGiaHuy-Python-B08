colors = ['red', 'blue', 'yellow', 'green']
print(*colors, sep=", ")
n = input("Nhập thêm màu vào list:")
colors.append(n)
print(*colors,sep=", ")
