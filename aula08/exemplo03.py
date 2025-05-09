# Cadastra
def cadastra_pessoa(num):
    for i in range(num):
        nome = input("Digite o nome do vendedor: ")
        vl = float(input("Digite o valor da venda: "))

        pessoa = {
            'Nome': nome,
            'Valor': vl,
        }

        lst_cadastro.append(pessoa)

def calcula_total_media():
    tot = 0
    for pessoa in lst_cadastro:
        tot += pessoa['Valor']

    med = tot / len(lst_cadastro)
    return tot, med


def buscar_maior():
    maior = 0
    vendedor = ''

    for v in lst_cadastro:
        if v['Valor'] > maior:
            maior = v['Valor']
            vendedor = v['Nome']

    return maior, vendedor

# BUSCAR NOME DO VENDEDOR


def buscar_vendedor(nome):
    resposta = ''
    valor = 0

    for cadastro in lst_cadastro:
        if cadastro['Nome'] == nome:
            resposta = cadastro['Nome']
            valor = cadastro['Valor']

        return resposta, valor
    return resposta, valor


# EXEMPLO 01 - CADASTRA FUNCIONARIO
lst_cadastro = []

qtd = int(input("Quantas pessoas? "))
cadastra_pessoa(qtd)
print(lst_cadastro)
# ---------------------------------------------------------------


# EXEMPLO 02 - TOTAL E MÉDIA
total, media = calcula_total_media()
print(30*'=')
print(f'Total: {total}')
print(f'Média: {media}')

# EXEMPLO 03 - MAIOR VALOR E VENDEDOR
maior_venda, maior_vendedor = buscar_maior()
print(f'Maior Venda: {maior_venda}')
print(f'Maior Vendedor: {maior_vendedor}')

# EXEMPLO 04 - BUSCAR VENDEDOR
vendedor = input('Informe o nome do Vendedor: ')
nome_vendedor, valor = buscar_vendedor(vendedor)

if nome_vendedor:
    print(f'O nome do vendedor é {nome_vendedor}')
    print(f'o valor da venda é R${valor}')
else:
    print('Vendedor não localizado!')
