# Відділ кадрів. База даних про співробітників фірми: паспортні дані, освіта, спеціальність, посада, оклад. Організувати вибір за довільним запитом. Дані зберігаються в масиві.

def serch(choose, da):
    if choose == 1:
        for i in range(len(info)):
            if info[i]["name"] == da:
                print(info[i])
    if choose == 2:
        for i in range(len(info)):
            if info[i]["grade"] == da:
                print(info[i])
    if choose == 3:
        for i in range(len(info)):
            if info[i]["Specialization"] == da:
                print(info[i])
    if choose == 4:
        for i in range(len(info)):
            if info[i]["posada"] == da:
                print(info[i])


info = []
while True:
    print("1:All info \n2:Set info \n3:Find worker\n4:Exit")
    print('---')
    choose = int(input('Choose what to do:'))
    while choose > 4 or choose <= 0:
        choose = int(input('try again'))

    if choose == 1:
        print(info)
    elif choose == 2:
        name = input("Enter name: ")
        grade = input("Enter your grade : ")
        specialization = input("Enter specialization: ")
        posada = input("Enter posada : ")
        new = {"name": '', "grade": '', "Specialization": '', "posada": ''}

        new["name"] = name
        new["grade"] = grade
        new["specialization"] = specialization
        new["posada"] = posada
        info.append(new)
        print('---')
    elif choose == 3:
        print('1:Name\n2:Grade\n3:Specialization\n4:posada')
        choose2 = int(input('Choose what to do:'))
        while choose2 > 4 or choose2 <= 0:
            choose2 = int(input('try again'))
        if choose2 == 1:
            da = input("Choose Name: ")
            serch(1, da)

        if choose2 == 2:
            da = input(" Choose Grade : ")
            serch(2, da)
        if choose2 == 3:
            da = input(" Choose specialization: ")
            serch(3, da)
        if choose2 == 4:
            da = input("Choose posada: ")
            serch(4, da)
        print('---')
    elif choose == 4:
        break