Harry_Potter = {
    "name" : "Harry Potter",
    "time" : 2000,
    "character" : ['Harry Potter', 'Hermione Granger', 'Ronnal Weasley', 
    'Draco Mafoy', 'Albus Dumbledore']
    
}
m = 0
print("Chọn nhân vật chính của truyện Harry Potter:")
A = Harry_Potter["character"][1]
B = Harry_Potter["character"][0]
C = Harry_Potter["character"][3]
D = Harry_Potter["character"][2]
print("A",A)
print("B",B)
print("C",C)
print("D",D)
  
n = input("Nhập câu trả lời:")

if n.upper()=="B":
    print("Bạn đã trả lời đúng")
    m = m+1
else:
    print("Bạn đã trả lời sai")
    
print("Chọn thời gian truyện được phát hành:")
print("A",2002)
print("B",2001)
print("C",2003)
print("D",Harry_Potter["time"])

n = input("Nhập câu trả lời:")

if n.upper()=="D":
    print("Bạn đã trả lời đúng")
    m = m+1
else:
    print("Bạn đã trả lời sai")



print("Chọn tên của truyện:")
print("A","Sherlock Holmes")
print("B",Harry_Potter["name"])
print("C","Conan")
print("D","Yaiba")

n = input("Nhập câu trả lời:")
if n.upper()=="B":
    print("Bạn đã trả lời đúng")
    m = m+1
else:
    print("Bạn đã trả lời sai")


print("Số câu bạn trả lời đúng là:",m)
print("Tỉ lệ trả lời đúng của bạn là:",m/3*100,"%")


