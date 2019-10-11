tieu_su = {
    "name" : "Huy",
    "Tuổi" : 15,
    "Sở thích" : "Đọc sách",
    "Description" : "Handsome"
}

del tieu_su["Tuổi"]
print(tieu_su)

n = input("Nhập key cần xóa:")
del tieu_su[n]
print(tieu_su)