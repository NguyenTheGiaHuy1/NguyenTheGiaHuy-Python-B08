Harry_Potter = {
    "name" : "Harry Potter",
    "time" : 2000,
    "character" : ['Harry Potter', 'Hermione Granger', 'Ronnal Weasley', 
    'Draco Mafoy', 'Albus Dumbledore']
    
}


Harry_Potter["Nhà sản xuất"] = "Disney"
Harry_Potter["Quốc gia"] = "Anh"

for k,v in Harry_Potter.items():
    print(k,"-",v)

Harry_Potter["character"] = ['Sherlock Holmes', 'Watson', 'Conan Doyle']
print(Harry_Potter)
Harry_Potter["character"].append('Bohemia')
print(Harry_Potter)
Harry_Potter["character"].pop(0)
print(Harry_Potter)
print(Harry_Potter["character"][1])
    
for i,a in enumerate(Harry_Potter["character"]):
    print(i,",",a)
for k,v in Harry_Potter.items():
    if k == "character":
        for i,a in enumerate(Harry_Potter["character"]):
            print(k,i+1,":",a)
    else:
        print(k,v)
