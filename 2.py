# Довідник гравця. База даних ігор: назва гри, вартість гри, жанр, кількість рівнів.  Організувати вибір за довільним запитом. Дані зберігаються в масиві записів, який створюється динамічно.

def serch(choose, da):
    if choose == 1:
        for i in range(len(games)):
            if games[i]["title"] == da:
                print(games[i])
    if choose == 2:
        for i in range(len(games)):
            if games[i]["price"] == da:
                print(games[i])
    if choose == 3:
        for i in range(len(games)):
            if games[i]["genre"] == da:
                print(games[i])
    if choose == 4:
        for i in range(len(games)):
            if games[i]["ammount_of_levels"] == da:
                print(games[i])


games = []
while True:
    print("1:All games \n2:Add game \n3:Find game\n4:Exit")
    print('---')
    choose = int(input('Choose what to do:'))
    while choose > 4 or choose <= 0:
        choose = int(input('try again'))

    if choose == 1:
        print(games)
    elif choose == 2:
        title = input("Enter title: ")
        price = input("Enter price: ")
        genre = input("Enter genre: ")
        levels = input("Enter ammout of levels : ")
        new = {"title": '', "price": '', "genre": '', "ammount_of_levels": ''}

        new["title"] = title
        new["price"] = price
        new["genre"] = genre
        new["ammount_of_levels"] = levels
        games.append(new)
        print('---')
    elif choose == 3:
        print('1:title\n2:price\n3:genre\n4:ammount_of_levels')
        choose2 = int(input('Choose what to do:'))
        while choose2 > 4 or choose2 <= 0:
            choose2 = int(input('try again'))
        if choose2 == 1:
            da = input("Choose title: ")
            serch(1, da)

        if choose2 == 2:
            da = input(" Choose price : ")
            serch(2, da)
        if choose2 == 3:
            da = input(" Choose genre: ")
            serch(3, da)
        if choose2 == 4:
            da = input("Choose ammount_of_levels: ")
            serch(4, da)
        print('---')
    elif choose == 4:
        break