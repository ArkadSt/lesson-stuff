import random
random_dice_throws = [random.randint(1,6) + random.randint(1,6) for _ in range(1000)] # сгенерировать список из бросков кубиков. бросаются 2 кубика вместе. 1000 бросков.
#print(random_dice_throws)

#statistics = {i: random_dice_throws.count(i) for i in range(2, 13)} # создать статистику (словарь) где ключ - выпавшая цифра, значение - сколько раз эта цифра выпала.

statistics = {}
for i in random_dice_throws:
    statistics[i] = statistics.get(i, 0) + 1
    
print(statistics)


