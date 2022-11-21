while True:
    command = input('выберите одну из этих комманд: Time, Math, Step')
    if command=='exit':
        break
    elif command=='Time':
        a = int(input('введите количетсво предметов:'))
        p = [0,0,5,10,25,30,35,50,55,60,75] #[0,5,5,15,5,5,15,5,5,15]
        z = a*45 + p[a]
        print(f'ваш {a} урок закончится в:'z//60 + 8, z%60)
    elif command=='Math':
        i = input('введите все ваши оценки по математике через пробел:').split()
        nums = list(map(int, i))
        c = int(sum(nums)/len(nums))
        print(f'Ваша средняя оценка по математике: {c}')
    elif command=='Step':
        v = int(input('введите длину кабинета в метрах:'))
        x = int((v*10)/5)
        print(f'вам необходимо сделать {x} шагов')
    else:
        print('вы некорректно ввели команду')