import random

# Generar un entero aleatorio
numeroRandom = random.randint(1, 20)
print(numeroRandom)

#Elegir colore aleatorios
colors = ['rojo', 'amarillo', 'verde']

colorRandom = random.choice(colors)

print(colorRandom)

# Barajar cartas
cards = ['♣️', '♠️', '♦️', '❤️']
random.shuffle(cards)
print(cards)