#change difficulty to change how much health a player gets

import random

health = 50

difficulty = 3

potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)
