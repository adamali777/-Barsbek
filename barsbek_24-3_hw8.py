object = []
counter = 0
left = 1
right = 100
while True:
    middle = int((left + right) / 2)
    object2 = input(f'Ваше число {middle}?')
    object2 = object2.lower()
    object.append(middle)
    counter += 1
    if object2 == 'больше':
        left = middle + 1
    elif object2 == 'меньше':
        right = middle - 1
    elif object2 == 'да':
        left = middle
        right = middle
        break
    else:
        'вы ввели неверно'
with open('results.txt', 'w') as file:
    file.write(f'{counter},{object},{left}')
