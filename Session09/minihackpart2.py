colors = ['red', 'blue', 'yellow', 'green']
print(*colors, sep=", ")
n = int(input("Nhập vị trí màu cần xem:"))
print(colors[n])

while True:
    delete = input("Nhập vị trí cần xóa:")

    if delete.isdigit():
        colors.pop(int(delete))
    elif delete.isalpha():
        colors.remove((delete))
    else :
        print("Không hợp lệ.")
    for i,x in enumerate(colors):
        print(i,".",x)

