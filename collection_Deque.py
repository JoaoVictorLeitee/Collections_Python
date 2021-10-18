"""
Módulo collection = Deque -> lista de high performance
Collections = High-perfomance Container Datetypes
"""
from collections import deque

deq = deque('Python')
print(deq)

deq.appendleft(deque('Programador'))
print(deq)

deq.append('Jr')
print(deq)

#pop ou popleft (remover)