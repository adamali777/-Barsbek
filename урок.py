class Hero:
    head = 1
    ability = True
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
    def heal(self,plus):
        print(self.hp + plus)
    def two_damage(self,x2):
        print(self.damage * x2)
    def dreetings(self):
        print('my name is ' + self.nickname)
    def brand_phrase(self):
        print('good will win')
h1 = Hero(name='Sultan', nickname='SultanChay', hp=100, damage=30)
print(1, h1.name, h1.nickname, h1.hp, h1.damage)
h1.heal(100)
h2 = Hero(name='Adik', nickname='Adugene', hp=30, damage=50)
print(2, h2.name, h1.nickname, h2.hp, h2.damage)
h2.two_damage(2)
h3 = Hero(name='Asulai', nickname='Asu', hp=500, damage=30)
print(3, h3.name, h3.nickname, h3.hp, h3.damage)
h3.dreetings()
h4 = Hero(name='Max', nickname='MaxiChay', hp=1000, damage=10)
print(4, h4.name, h4.nickname, h4.hp, h4.damage)
h4.brand_phrase()