P = {
    "x" : 5,
    "y" : 5
}
K = {
    "x" : 6,
    "y" : 6
}
E ={
    "x" : 2,
    "y" : 1
}
W ={
    "x" : 3,
    "y" : 1
}









Move = {
    "W" : 1,
    "A" : 1,
    "S" : 1,
    "D" : 1
}

check =0 
# tạo bản đồ
while True:
    for y in range(10):
        for x in range(10):
            if x ==P["x"]and y ==P["y"]:
                print('P', end=" ")
            elif x==K["x"]and y==K["y"]:
                print('K', end=" ") 
            elif x==E["x"]and y==E["y"]:
                print('E', end=" ") 
            elif x==W["x"]and y==W["y"]:
                print('W', end=" ")
            else:
                print("-", end=" ")
        print()
    
    # kt chìa khóa
    if check ==1:
        if P["x"]==E["x"] and P["y"]==E["y"]:
            print("Bạn đã qua bàn.")
            break 
    else:
        print("Bạn phải có chìa khóa để qua cửa.")  
   
    
    # di chuyển
    n = input("Nhập hướng di chuyển:")
    if n.upper()=="W":
        P["y"] = P["y"] -Move[n.upper()]
    elif n.upper()=="A":
        P["x"] = P["x"] -Move[n.upper()]
    elif n.upper()=="S":
        P["y"] = P["y"]+Move[n.upper()]
    elif n.upper()=="D":
        P["x"] = P["x"]+Move[n.upper()]
    
    
    
    # giới hạn bản đồ
    if P["x"]>10 or P["x"]<0:
        print("Bạn không thể đi ra khỏi bản đồ. ")
        if n.upper()=="A":
            P["x"] = P["x"]+Move[n.upper()]
        elif n.upper()=="D":
            P["x"] = P["x"]-Move[n.upper()]
    elif P["y"]>10 or P["y"]<0:
        print("Bạn không thể đi qua tường.")
        if n.upper()=="W":
            P["y"] = P["y"] +Move[n.upper()]
        elif n.upper()=="S":
            P["y"] = P["y"]-Move[n.upper()]
    

   
    
    # tạo biến check chìa
    if P["x"]==K["x"] and P["y"]==K["y"]:
        print("Bạn đã có chìa khóa.")
        K["x"] = 10
        K["y"] = 10
        check =1
    
    
# tạo tường    
    elif P["x"]==W["x"] and P["y"]==W["y"]:
        print("Bạn không thể đi qua tường.")
        if n.upper()=="W":
            P["y"] = P["y"] +Move[n.upper()]
        elif n.upper()=="A":
            P["x"] = P["x"] +Move[n.upper()]
        elif n.upper()=="S":
            P["y"] = P["y"]-Move[n.upper()]
        elif n.upper()=="D":
            P["x"] = P["x"]-Move[n.upper()]
    











# bàn 2
P = {
    "x" : 5,
    "y" : 5
}
K = {
    "x" : 6,
    "y" : 6
}
E ={
    "x" : 7,
    "y" : 7
}
W ={
    "x" : 3,
    "y" : 5
}
K2 = {
    "x" : 8,
    "y" : 8
}
check2=0 
while True:
    for y in range(10):
        for x in range(10):
            if x ==P["x"]and y ==P["y"]:
                print('P', end=" ")
            elif x==K["x"]and y==K["y"]:
                print('K', end=" ") 
            elif x==K2["x"] and y==K2["y"]:
                print('K', end=" ")
            elif x==E["x"]and y==E["y"]:
                print('E', end=" ") 
            elif x==W["x"]and y==W["y"]:
                print('W', end=" ")
            else:
                print("-", end=" ")
        print() 


# kt 2 chìa khóa
    if check ==1 and check2==1:
        if P["x"]==E["x"] and P["y"]==E["y"]:
            print("Bạn đã qua bàn.")
            break 
    else:
        print("Bạn phải có cả 2 chìa khóa để qua cửa.")  
   
    
    # di chuyển
    n = input("Nhập hướng di chuyển:")
    if n.upper()=="W":
        P["y"] = P["y"] -Move[n.upper()]
    elif n.upper()=="A":
        P["x"] = P["x"] -Move[n.upper()]
    elif n.upper()=="S":
        P["y"] = P["y"]+Move[n.upper()]
    elif n.upper()=="D":
        P["x"] = P["x"]+Move[n.upper()]



    # giới hạn bản đồ
    if P["x"]>10 or P["x"]<0:
        print("Bạn không thể đi ra khỏi bản đồ. ")
        if n.upper()=="A":
            P["x"] = P["x"]+Move[n.upper()]
        elif n.upper()=="D":
            P["x"] = P["x"]-Move[n.upper()]
    elif P["y"]>10 or P["y"]<0:
        print("Bạn không thể đi qua tường.")
        if n.upper()=="W":
            P["y"] = P["y"] +Move[n.upper()]
        elif n.upper()=="S":
            P["y"] = P["y"]-Move[n.upper()]


    # tạo biến check 2 chìa
    if P["x"]==K["x"] and P["y"]==K["y"]:
        print("Bạn đã có chìa khóa.")
        K["x"] = 10
        K["y"] = 10
        check =1
    elif P["x"]==K2["x"] and P["y"]==K2["y"]:
        print("Bạn đã có chìa khóa.")
        K2["x"] = 11
        K2["y"] = 11
        check2 =1
    
    
    
    
    # tạo tường    
    elif P["x"]==W["x"] and P["y"]==W["y"]:
        print("Bạn không thể đi qua tường.")
        if n.upper()=="W":
            P["y"] = P["y"] +Move[n.upper()]
        elif n.upper()=="A":
            P["x"] = P["x"] +Move[n.upper()]
        elif n.upper()=="S":
            P["y"] = P["y"]-Move[n.upper()]
        elif n.upper()=="D":
            P["x"] = P["x"]-Move[n.upper()]
         
         




        
    

    







