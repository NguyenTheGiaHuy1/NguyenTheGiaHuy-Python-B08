S = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
Tên = ['Sơn Tây', 'Ba Đình', 'Bắc Từ Liêm', 'Cầu Giấy', 'Đống Đa', 'Hai Bà Trưng']
Dan  = [150300, 247100, 333300, 266800, 420900, 318000]
mat_do = []

for i,a in enumerate(Dan):
    m = float(a/S[i])
    mat_do.append(m)
print(mat_do)
print("Mật độ dân cư trung bình là :",sum(Dan)/len(Tên))

