# Crie uma lista apenas com elementos numéricos
numeros = [1,2,3,4,5,6,7,8,9,0]
print(numeros)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_int = [1,14,1000,-2,0,12,-15000,200]
lista_float = [3.14,-4.23,15.10,6.459,-12.56]
lista_str = ['python','x','doce','''Hoje estou fazendo novos exercícios sobre python''']
lista_bool = [True, False]
lista_operadores = ['+', '-', '*', '/', '//', '**', '%']

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista_int[:5])
print(lista_float[:5])
print(lista_str[:5])
print(lista_bool[:5])
print(lista_operadores[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista_int[::2])
print(lista_float[::2])
print(lista_str[::2])
print(lista_bool[::2])
print(lista_operadores[::2])

# Remova da lista o último item
lista_int.pop()
lista_float.pop()
lista_str.pop()
lista_bool.pop()
lista_operadores.pop()

# Insira na lista um novo item
lista_int.append(10)
lista_float.append(7.89)
lista_str.append('novo item')
lista_bool.append(True)
lista_operadores.append('**')

# Remova da lista um item específico
lista_int.remove(10)
lista_float.remove(7.89)
lista_str.remove('novo item')
lista_bool.remove(True)
lista_operadores.remove('**')

# Listas atualizadas
print(lista_int)
print(lista_float)
print(lista_str)
print(lista_bool)
print(lista_operadores)


lista_int.append(390, 84)
print(lista_int)


