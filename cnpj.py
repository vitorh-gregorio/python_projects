"""""
Módulo para gerar ou validar CNPJs
"""""
import re
import random


def remove_caracteres(cnpj_informado):
    return re.sub(r'[^0-9]', '', cnpj_informado)


def part_cnpj(cnpj_informado):
    cnpj_validacao = cnpj_informado[0:12]
    return cnpj_validacao


def valida(cnpj_informado):
    cnpj_informado = remove_caracteres(cnpj_informado)
    cnpj_validacao = part_cnpj(cnpj_informado)
    novo_cnpj = cnpj_validacao + str(define_digito1(cnpj_informado)) + str(define_digito2(cnpj_informado))
    if novo_cnpj == cnpj_informado:
        return 'CNPJ válido!'
    else:
        return 'CNPJ inválido'


def define_digito1(cnpj_informado):
    cnpj_validacao = part_cnpj(cnpj_informado)
    lista_produto = []
    mult = 5
    for i in cnpj_validacao:
        if mult < 2:
            mult = 9
        produto = int(i) * mult
        lista_produto.append(produto)
        mult -= 1
    d1 = 11 - (sum(lista_produto) % 11)
    d1 = 0 if d1 > 9 else d1
    return d1


def adiciona_d1_cnpj(cnpj_informado):
    cnpj_validacao = part_cnpj(cnpj_informado)
    lista = []
    d1 = define_digito1(cnpj_informado)
    for i in cnpj_validacao:
        lista.append(i)
    lista.append(d1)
    return lista


def define_digito2(cnpj_informado):
    lista = adiciona_d1_cnpj(cnpj_informado)
    mult = 6
    lista_produto = []
    for i in lista:
        if mult < 2:
            mult = 9
        produto = int(i) * mult
        lista_produto.append(produto)
        mult -= 1
    d2 = 11 - (sum(lista_produto) % 11)
    d2 = 0 if d2 > 9 else d2
    return d2


def gera_cpf():
    lista_aleatorios = []
    for i in range(8):
        n_aleatorio = str(random.randint(0, 9))
        lista_aleatorios.append(n_aleatorio)
    lista_aleatorios.append('0001')
    cnpj_gerado = ''.join(map(str, lista_aleatorios))
    d1 = define_digito1(cnpj_informado=cnpj_gerado)
    d2 = define_digito2(cnpj_informado=cnpj_gerado)
    cnpj_gerado = cnpj_gerado + str(d1) + str(d2)
    return cnpj_gerado