n = ['Toán', 'Lý', 'Hóa', 'Lịch sử', 'Sinh', 'Tin']
n.append('Công nghệ')
print(*n, sep= ', ')
print("Phần tử đầu tiên, cuối cùng, và gần cuối:")
print(n[1].upper())
print(n[-1].upper())
print(n[-2].upper())