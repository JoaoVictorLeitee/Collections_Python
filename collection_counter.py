"""
Módulo collection = Counter (Contador)
Collections = High-perfomance Container Datetypes
"""

from collections import Counter

lista = [1, 2, 2, 3, 3, 4, 1, 2, 3, 2, 4, 5, 6, 8, 7, 8, 5, 2, 1, 4, 5, 6, 9]
res = Counter(lista)
print(type(res))
print(res)

print(Counter('Programação Python'))

texto = """ a jogada futebolística conhecida como chute de bicicleta (imagem) é chamada de chilena nos países hispânicos, 
enquanto na Noruega recebe o nome de brassespark, que significa "chute brasileiro"?"""

palavras = texto.split()
res = Counter(palavras)
print(res)
print(res.most_common(5))