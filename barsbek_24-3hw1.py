class Hero:
    head = 1
    ability = True
    def __init__(self,name,nickname,hp,damage):
      self.name=name
      self.hp=hp
      self.nickname=nickname
      self.damage=damage
    def heal(self,hp):
      print(self.hp + 100)
    def two_damage(self, x2):
      print(self.damage * x2)
    def dreetings(self):
        print('my name is ' + self.nickname)
    def brand_phrase(self):
        print('good will win')
h1 = Hero(name = 'Barsbek', nickname = 'Kagan', hp = 100 , damage = 70 )
h1.heal(100)
print(h1.name,h1.nickname,h1.hp,h1.damage)
h2 = Hero(name = 'Terminator', nickname = 'Termos', hp =50, damage = 50)
print(h2.name , h2.nickname , h2.hp , h2.damage)
h2.two_damage(2)
h3 = Hero(name = 'Abu', nickname = 'Bandit', hp = 10, damage = 90)
print(h3.name , h3.nickname , h3.hp , h3.damage)
h3.dreetings()
h4 = Hero(name = 'Dead Inside', nickname = 'Altuha', hp = 5 , damage = 10)
print(h4.name , h4.nickname , h4.hp , h4.damage)
h4.brand_phrase()




