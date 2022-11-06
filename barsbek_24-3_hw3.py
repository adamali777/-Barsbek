gl = 'УуЕеЫыАаОоЭэЯяИиЮюё' 'AaEeOoYyIiUu'
sog = 'ЙйЦцКкНнГгШшЩщЗзХхЪъФфВвПпРрЛлДдЖжЧчСсМмТтЬьБб'  'QqWwRrTtPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm'

while True:
     a = 0
     s = 0
     d = 0
     world = input("Введите слово: ")
     if world == 'exit' or world == 'выход':
             print('программа завершается!')
             break
     for i in world:
         if (i in gl) or (i in sog):
             d = int(d)
             d += 1
         if i in gl:
            a = int(a)
            a += 1
         if i in sog:
            s = int(s)
            s += 1
     count = len(world)
     print('Количество букв:', count)
     z = 100 * a / (a + s)
     x = 100 * s / (a + s)
     print('Количество гласных букв:', len([c for c in world if c in 'УуЕеЫыАаОоЭэЯяИиЮюё' 'AaEeOoYyIiUu']))
     print('Количество согласных букв:', len([x for x in world if x in 'ЙйЦцКкНнГгШшЩщЗзХхЪъФфВвПпРрЛлДдЖжЧчСсМмТтБб'  'QqWwRrTtPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm']))
     print(f"согласные: {round(x, 2)}% , гласные: {round(z, 2)}%")
