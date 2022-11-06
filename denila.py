# #циклы: for, while
# #break , continue
# word= 'kyrgyzstan'
# counter = 1
# for letter in word:
#     print(counter , letter)
#
#     if letter == 'z':
#         break
import time
# Показать любовные ключевые слова
words = 'Sultan'
print("     ")
print("     ")
print("     ")
print("      ")
for item in words.split():
    # Чтобы добиться эффекта распечатки пробелов между символами, добавьте сюда: item = item + ''
    letterlist = []#letterlist - это общий список всех печатных символов, который содержит подсписок y list_X
    for y in range(12, -12, -1):
        list_X = []#list_X - список напечатанных символов на оси X, который содержит строку букв
        letters = ''#letters - это строка в list_X, которая фактически является всеми символами, которые будут напечатаны в этой строке
        for x in range(-30, 30):# * - умножение, ** - сила
            expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <= 0:
                letters += item[(x-y) % len(item)]
            else:
                letters += ' '
        list_X.append(letters)
        letterlist += list_X
    print('\n'.join(letterlist))
    time.sleep(150);