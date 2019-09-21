n = input("Nhập tên đăng nhập của bạn:")
while True:
    m = input("Nhập mật khẩu của bạn:")
    m_ = input("Nhập lại mật khẩu:")
    if m!=m_:
        print("Mật khẩu sai")
    elif m.isalpha() or m.isdigit():
        print("Mật khẩu không thỏa mãnas")
    elif len(m)<=8:
        print("Mật khẩu không thỏa mãn")
    else:
        print("Mật khẩu đúng")
        break
while True:

    x = input("Nhập email của bạn:")
    if '@gmail.com' in x:
        print("Mật khẩu đúng")
        break
    else:
        print("Mật khẩu sai")