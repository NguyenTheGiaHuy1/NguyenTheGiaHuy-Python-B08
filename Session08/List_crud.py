n = ['Toán', 'Công nghệ', 'Hóa', 'Văn']
n.append('Tin'), n.append('Sinh'), n.append('Anh')
    
while True:  
    m = list(input("Nhập thao tác cần thực hiện với List:"))
        
   
    if 'c' in m:
        a = input("Nhập thứ bạn yêu thích:")
        n.append(a)
        print(*n,sep= ", ")
    elif 'r' in m:
        if n==[]:
            print("List rỗng, mời kiểm tra lại.")
        else:
            for i in n:
                print(i)
    elif 'u' in m:
        x = int(input("Nhập vị trí cần cập nhật:"))
        y = input("Nhập nội dung cần thay đổi:")
        n[x]=y
        print(*n,sep=", ")
    elif 'd' in m:
        z = int(input("Nhập vị trí muốn xóa:"))
        n.pop(z)
        print(n)