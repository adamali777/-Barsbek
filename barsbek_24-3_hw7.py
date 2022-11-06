ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
evens2 = list(map(lambda x: x ** 2, evens))
print(evens2)
def one(lst=ten):
    while True:
        three = (input('Введите число:'))
        if three == 'exit':
            break
        try:
            print(lst[int(three)])
        except:
            print(input(f'Вводите числа только от 0 до {len(lst)-1}'))
one()