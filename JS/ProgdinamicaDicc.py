# Ralizado por luis h
planetas_lunas = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
# Se obtienen una lista de lunas y numero de planetas
lunas = planetas_lunas.values()
total_planetas = len(planetas_lunas.keys())
print("Numero de planetas:", total_planetas)
print('Solo saturno tiene', planetas_lunas.get('saturn'), 'lunas')
total_lunas = 0
for luna in lunas:
    total_lunas = total_lunas + luna
print("Numero de lunas:", total_lunas)

average = total_lunas / total_planetas

print(f'Cada planta tiene un promedio de {round(average, 2)} lunas')
