import random

HP=100
eHP=100
N=1
while HP > 0 and eHP > 0:
    print('Номер хода:', N)
    roll = random.randint(-2, 10)
    if roll >= 1:
            damage = random.randint(0, 20)
            eHP = eHP - damage
            print("У врага осталось ", eHP, " ХП")
    else:
            print("Ты промахнулся")
    if eHP > 0:
        eroll= random.randint(-2, 10)
        if eroll >= 1:
                edamage = random.randint(0, 20)
                HP = HP - edamage
                print("У тебя осталось ", HP, " ХП")
        else:
                print("Враг промахнулся")
    else:
        break
    N=N+1
if HP <= 0:
    print('Ты погиб')
if eHP <= 0:
    print('Враг погиб')