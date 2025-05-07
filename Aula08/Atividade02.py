produto = {
    'Nome': 'Notebook',
    'Preço': 3500.00,
    'Estoque': 15,
}

del produto['Estoque']
print(produto)
produto['Preço'] = 4000.00

print(f"{produto['Nome']}, R${produto['Preço']}")
