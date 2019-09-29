n = ['Toán', 'Lý', 'Hóa', 'Lịch sử', 'Sinh', 'Tin']

import random
m = random.randint(0,len(n)-1)
ran = list(n[m])
random.shuffle(ran) 
for i in ran:
    print(i)
d = input("Mời đoán từ:")
if d in n:
    print("Đoán đúng.")
else :
    print("Đoán sai.")

