
salary_table1 = {
        "name": "Huy",
        "role": "Waiter",
        "hours": 12,
        "salary-per": 0.8
}

salary_table2 = {
        "name" : "Tung",
        "role" : "cook",
        "hours" : 24,
        "salary-per" : 1.5
}

salary_table3 = {
        
        "name" : "Minh Đức",
        "role" : "manage",
        "hours" : 20,
        "salary-per" : 2
}

salary_table = [salary_table1, salary_table2, salary_table3]

for i in range(len(salary_table)):
    print(salary_table[i]['hours'] * salary_table[i]['salary-per'])


salary_table[1] = {
    "name" : "Huyền",
    "role" : "waitress",
    "hours" : 14,
    "salary-per" : 1 
}
print(salary_table)

salary_table.pop(2)
print(salary_table)

for i in range(len(salary_table)):
    print(salary_table[i])
    
for i in range(len(salary_table)):
    print(salary_table[i]['hours'] * salary_table[i]['salary-per'] * 30)


n = 0
a = 0
for i in range(len(salary_table)):
    n = salary_table[i]['hours'] * salary_table[i]['salary-per'] * 30
    a = n+a
    print(a)


