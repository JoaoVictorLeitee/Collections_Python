"""
Módulo collection = Named Tuple
Collections = High-perfomance Container Datetypes
"""
from collections import namedtuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])
#cachorro = namedtuple('cachorro', 'idade raça nome')
#ou cachorro = namedtuple('cachorro', 'idade, raça, nome')

ray = cachorro(idade=2, raça='Pitbull', nome='Dagan')
print(ray)
print(ray[0])
print(ray[1])
print(ray[2])
#ou
print('-------------------------------')
print(ray.idade)
print(ray.raça)
print(ray.nome)

print(ray.index('Dagan'))
print(ray.count('Dagan'))