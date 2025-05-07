def cadastra_pessoa(num):
    for i in range(num):
        nome = input("Digite o nome do vendedor: ")
        vl = input("Digite o valor da venda: ")

        pessoa = {
            'Nome': nome,
            'Valor': vl,
        }    

        lst_cadastro.append(pessoa)


# Principal
lst_cadastro = []

qtd = int(input("Quantas pessoas? "))
cadastra_pessoa(qtd)
print(lst_cadastro)
