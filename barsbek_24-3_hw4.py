numbers = []
letters = []
data_tuple = ('h', 6.13,'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = [i for i in data_tuple if type(i) not in [int, float]]
numbers = [i for i in data_tuple if type(i) not in [bool, str]]
numbers.remove(6.13)
del letters [4]
numbers.insert(2,2)
numbers.sort()
numbers = [i*i for i in numbers ]
letters.insert(-9,True)
letters.reverse()
letters[letters.index('g')] =('G')
letters[letters.index('C')] =('c')
letters = tuple (letters)
numbers = tuple (numbers)
print(f"{letters}\n{numbers}\n")