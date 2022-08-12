"""""
Gerador e validador de CNPJs
- É necessário utilizar o módulo cnpj.py
"""""
import cnpj

while True:
    entrada = input('Digite VALIDAR para validar um CNPJ ou GERAR para gerar um novo: ').upper()
    if entrada == 'VALIDAR':
        cnpj_informado = input('Digite o CNPJ que deseja validar: ')  # '04.252.011/0001-10'
        print(cnpj.valida(cnpj_informado))
    elif entrada == 'GERAR':
        print(cnpj.gera_cpf())
    else:
        print('Favor digitar apenas VALIDAR ou GERAR.')