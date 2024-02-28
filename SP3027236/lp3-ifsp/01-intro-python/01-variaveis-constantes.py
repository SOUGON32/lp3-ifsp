# identificadores
# letra , números e +
# não pode ser palavra reservada: if, None, True, False
# case sensitive

Nome = "Pedro"
nome = "Pedro"

# variaves
# tudo em minusculo
# separador _
# Snake_case

idade = 20
pessoa_fisica = "Marcio"
pessoa_juridica = 'Paula LTDA'
imposto_renda = 2200.45

# E o tipo?
# java
# String Nome = "Pedro"
# int idade = 20
# no python temos inferência de tipo 
# O tipo será definido com base no valor(literal)

idade = 20 # int
nome = "Pedro" # str

# Constantes
# não constante no Python
# Convenção: nome em maiúsculo

PI = 3.14

# Comentários de única linha

'''
Comentário de múltiplas linhas
'''

# docstring (comentário de documentação)
# documentar classe, módulos, funções, ...

def somar(número1, número2):
    '''
    Funçao que soma dois números
    :para numero1:  primeiro número
    :param numero2: segundo número
    :return: a soma dos números
    '''
    return numero1 + numero2

