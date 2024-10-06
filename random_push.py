import random

# Genera un número aleatorio entre 2 y 10
random_count = random.randint(2, 10)

# Escribe el número aleatorio en un archivo
with open('count.txt', 'w') as f:
    f.write(str(random_count))
