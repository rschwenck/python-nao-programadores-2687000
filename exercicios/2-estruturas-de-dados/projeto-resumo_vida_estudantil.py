# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e 
# imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual 
#    e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudantes = {}

estudantes['nome'] = input("Digite seu nome: ")
estudantes['ano_conheceu_linkedin'] = int(input("Digite o ano que conheceu o LinkedIn: "))
estudantes['ano_atual'] = int(input("Digite o ano atual: "))
cursos = input("Digite os cursos realizados no LinkedIn Learning separados por vírgula em ordem cronológica: ")
estudantes['cursos'] = [curso.strip() for curso in cursos.split(',')]   

# 2. Armazene esses dados em um dicionário


# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de 
#    anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

total_anos = estudantes['ano_atual'] - estudantes['ano_conheceu_linkedin']
total_cursos = len(estudantes['cursos'])    

print(
    f"Oi {estudantes['nome']}, você conheceu o LinkedIn em "
    f"{estudantes['ano_conheceu_linkedin']}. Nestes {total_anos} anos, "
    f"você realizou {total_cursos} cursos no LinkedIn Learning. "
    f"O primeiro curso foi '{estudantes['cursos'][0]}' e o último foi "
    f"'{estudantes['cursos'][-1]}'."
)