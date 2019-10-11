tieu_su = {
    "name" : "Huy",
    "Tuổi" : 15,
    "Sở thích" : "Đọc sách",
    "Description" : "Handsome"
}
tieu_su["Sở thích"] = "Chơi"
tieu_su["Tuổi"] = 16
tieu_su["Môn học yêu thích"] = "Hóa, Lý, Toán, Tin"
print(tieu_su)


y = input("Nhập value cần update:")
tieu_su["Description"] = y
print(tieu_su)