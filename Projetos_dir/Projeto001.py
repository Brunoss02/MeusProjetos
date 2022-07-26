"""
Funções (def) em Python - *args **kwargs -
Aula 16 (parte 3)
"""
# *args quando pode receber mais valores
# **kwargs posso definir por chaves os valores


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Hello {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


primeiro_valor = mestre(saudacao, 'Bruno', saudacao='Have nice day,')
print(primeiro_valor)
