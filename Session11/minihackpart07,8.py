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
print(text_aventure["Gold"])
text_aventure["Backpack"].append("Flint Stone")
print(text_aventure)
text_aventure["Pocket"] = ['MonsterDex', 'Flashlight']
print(text_aventure)
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
for i in Skill:
    print(i)
a = 0
for i in Skill:
    print("Skill",a+1,":",i["Name"])  
    a+=1 


