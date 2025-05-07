aluno = {
    'Nome': 'Maria',
    'Idade': 29,
    'Curso': 'Medicina',
}

print(aluno)
print(aluno['Idade'])

aluno['Nome'] = 'Jesus'
print(aluno)
aluno['Email'] = 'jesus@glory.com'
print(aluno)

if 'Tel' in aluno:
    aluno.pop('Nome')

print(aluno)

# aluno.clear()
# print(aluno)

# del aluno
# print(aluno)

for chave, valor in aluno.items():
    print(chave, valor)
