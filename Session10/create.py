tieu_su = {
    "name" : "Huy",
    "Tuổi" : 15,
    "Sở thích" : "Đọc sách",
    "Description" : "Handsome"
}
tieu_su["Học lực"] = "Giỏi"
print(tieu_su)

x = input("Nhập Key:")
y = input("Nhập Value:")
tieu_su[x] = y
print(tieu_su)

for key, value in tieu_su.items():
    if key == "name":
        print(key)
    elif key == "Description":
        print(key)

a = input("Nhập Key :")

for key, value in tieu_su.items():
    if key == a:
        print(key)
    
