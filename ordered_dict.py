"""
Módulo collection = Ordered Dict
Collections = High-perfomance Container Datetypes
"""
from collections import OrderedDict

dicionario = {'a': '5', 'b': '4', 'c': '8', 'd': '7', 'e': '5'}
for chave, valor in dicionario.items():
    print(f'chave = {chave} : valor = {valor}')

print('-----------------------------------------------')

dicionario1 = OrderedDict({'a': '5', 'b': '4', 'c': '8', 'd': '7', 'e': '5'})
for chave, valor in dicionario1.items():
    print(f'chave = {chave} : valor = {valor}')

teste1 = OrderedDict({'a': '1', 'b': '2'})
teste2 = OrderedDict({'b': '2', 'a': '1'})
print(teste1 == teste2)