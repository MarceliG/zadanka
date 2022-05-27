import collections

li = ['a','b','c','d']

def przesun(lista):
    lista = collections.deque(lista)
    lista.rotate(2)
    return lista


print(przesun(li))
