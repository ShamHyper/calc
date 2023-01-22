import time

while True:

    first_symbol = int(input("Введите первое число: "))
    math = input("Введите математическое действие: ")
    second_symbol = int(input("Введите второе число: "))


    if math == "+" :
        sumbols1 = first_symbol + second_symbol
        print(first_symbol, math, second_symbol,"=", sumbols1)

    if math == "-" :
        sumbols2 = first_symbol - second_symbol
        print(first_symbol, math, second_symbol,"=", sumbols2)

    if math == "*" :
        sumbols3 = first_symbol * second_symbol
        print(first_symbol, math, second_symbol,"=", sumbols3)

    if math == "/" :
        sumbols4 = first_symbol / second_symbol
        print(first_symbol, math, second_symbol,"=", sumbols4)

    if math == "^" :
        sumbols4 = first_symbol ** second_symbol
        print(first_symbol, math, second_symbol,"=", sumbols4)       

    while True:
        flag = input('Ещё раз? [Да/Нет]: ')

        if flag == 'Да':
            break
        else:

            if flag == 'да':
                break
       
        if flag == 'Нет':
            quit() 
        else:       

            if flag == 'нет':
                quit()                       
        


