while True:
    n = input("Nhập mật khẩu:")

    if n.isalpha():
        print("Nhập lại mật khẩu.")
    elif (len(n))<8:
        print("Mật khẩu sai.")
    else :
        print("Mật khẩu đúng.")
        break
