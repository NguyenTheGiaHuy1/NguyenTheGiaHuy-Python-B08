n = ['Toán', 'Lý', 'Hóa', 'Lịch sử', 'Sinh', 'Tin']
n.append('Công nghệ')
print(*n, sep= ', ')
print("Phần tử đầu tiên, cuối cùng, và gần cuối:")
print(n[1],n[-1],n[-2],sep= ', ')