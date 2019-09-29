p = 0  
while True:    
    import random 
    n = random.randint(1,100)

    m = random.randint(1,100)
    j = random.randint(0,3)
    y = 0    
    x = random.randint(-1,1)
    if j==0:
        y = n+m

        print(n,"+",m,"=",x+y)
    elif j==1:
        y = n-m
        print(n,"-",m,"=",x+y)
    elif j==2:
        y = n/m
        print(n,":",m,"=",x+y)
    elif j==3:
        y = n*m
        print(n,"*",m,"=",x+y)
    
  

  

    
    a = input("Đúng hay sai")  
    
    if x == -1:
        if 's' in a:
            print("Bạn đã đúng.")
            p+=1
            print("Điểm của bạn",p)
        else:
            print("Bạn đã sai.")
            break
    elif x== 0:
        if 's' in a:
            print("Bạn đã sai.")
            break
        else:
            print("Bạn đã đúng.")
            p+=1
            print("Điểm của bạn",p)
    else:
        if 's' in a:
            print("Bạn đã đúng.")
            p+=1
            print("Điểm của bạn",p)
        else:
            print("Bạn đã sai")
            break



