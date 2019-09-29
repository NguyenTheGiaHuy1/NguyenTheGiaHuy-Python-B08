import random
n = input("Nhập từ của bạn:")

m = list(n)
random.shuffle(m)
for i in m:
    print(i.upper())
