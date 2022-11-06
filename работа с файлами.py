# file=open('file.txt','w',encoding='UTF-8')
# file.write('саламчик')
# file.close()
# with open ('file.txt','a') as file:
#     file.write('barsik')
# from time import sleep
# with open('file.txt','r',encoding='UTF-8') as file:
#     for i in file.read():
#         sleep(0.20)
#         print(i,  end='')
#         break
#      print(file.readlines(5))
with open ('results.txt','w') as file:
 for i in range (2, 10):
    for j in range(2,10):
        try:
            user = int(input(f'сколько будет{i}*{j}: '))
            right_answer = i * j
            with open ('results.txt','a') as file:
                if user == right_answer:
                    file.write(f'{i}*{j} = {user} (right_answer) right')

                    print('Правильно')
                else:
                    file.write(f'{i}*{j} = {user} (right_answer) wrong')
                    print(f"Неправильно! будет: ({right_answer})")
        except:
            print('введите только числа')


