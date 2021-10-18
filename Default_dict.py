"""
Módulo collection = Default Dict
Collections = High-perfomance Container Datetypes
Não retorna erro
"""
from collections import defaultdict

dicionario = {'curso': 'Programação Python'}
print(dicionario)
print(dicionario['curso'])

dicionario1 = defaultdict(lambda: 0)
print(dicionario1)

dicionario1['curso'] = 'Programação Python'
print(dicionario1)

print(dicionario1['outro'])

print(dicionario1)