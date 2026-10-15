# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá 
#    imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.

# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning

cursos=['Python: do Zero ao Primeiro App', 'Python para não programadores', 'Cloud Computing', 'AWS Cloud Architect','GenAI Claude']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas

curso1 = 'Python: do Zero ao Primeiro App'
curso2 = 'Python para não programadores'
curso3 = 'Cloud Computing'

# 3. Crie um dicionário vazio para armazenar a nota do curso

notas_cursos = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista

'''
if curso1 in cursos:
  print(f'O curso {curso1} está dentro da lista de cursos.')
if curso2 in cursos:
  print(f'O curso {curso2} está dentro da lista de cursos.')
if curso3 in cursos:
  print(f'O curso {curso3} está dentro da lista de cursos.')
'''
if curso1 and curso2 and curso3 in cursos:
  print(f'Os cursos {curso1}, {curso2} e {curso3} estão na lista de cursos.')
else:
  print('Um ou mais cursos estão faltando na lista de cursos.')

# 5. Se o curso estiver na lista, solicite uma nota para avaliação

if curso1 and curso2 and curso3 in cursos:
  nota1 = float(input(f'Digite uma nota para a avaliação do curso {curso1}: '))
  nota2 = float(input(f'Digite uma nota para a avaliação do curso {curso2}: '))
  nota3 = float(input(f'Digite uma nota para a avaliação do curso {curso3}: '))

  print('Notas inseridas com sucesso!!!')

# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

notas_cursos = {}
notas_cursos[curso1] = nota1
notas_cursos[curso2] = nota2
notas_cursos[curso3] = nota3

print('Dicionário atualizado!!!')
print(notas_cursos)