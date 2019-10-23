text_aventure={
    "Name" : "Light",
    "Age" : 17,
    "Strength" : 8,
    "Defense" : 10,
    "HP" : 100,
    "Backpack" : ['Shield', 'Bread Loaf'],
    "Gold" : 100,
    "Level" : 2
}
text_aventure["Gold"]=text_aventure["Gold"]+50
text_aventure["Backpack"].append("Flint Stone")
text_aventure["Pocket"] = ['MonsterDex', 'Flashlight']
Skill1 = {
    "Name" : "Tackle",
    "Minimum level" : 1,
    "Damage" : 5,
    "Hit rate" : 0.3
}
Skill2 = {
    "Name" : "Quick attack",
    "Minimum level" : 2,
    "Damage" : 3,
    "Hit rate" : 0.5
}
Skill3 = {
    "Name" : "Strong kick",
    "Minimum level" : 4,
    "Damage" : 9,
    "Hit rate" : 0.2
}
Skill = [Skill1, Skill2, Skill3]
Level = 3
print("Level hiện tại của bạn là:",Level)

a=0
for i in Skill:
    print("Skill",a+1,":",i["Name"])  
    a+=1
n = int(input("Mời chọn skill để sử dụng:"))
import random 
Hit_rate = random.random()
if Skill[n-1]["Minimum level"]<=Level:
    if Hit_rate<Skill[n-1]["Hit rate"]:
        print("Chiêu đã đánh trúng địch.")
        print("Lượng sát thương là",":",Skill[n-1]["Damage"])
    else:
        print("Chiêu đã đánh trượt địch.")
else:
    print("Bạn chưa đủ level để sử dụng skill này.")


