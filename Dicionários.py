coisas = {'Minas Gerais': 'MG', 'Rio Grande do Sul': 'RS', 'Espírito Santo': 'ES'}
cidades = {'MG': 'Belo Horizonte', 'RS':'Porto Alegre', 'ES': 'Vitória'}

print(list(coisas.items()))

print(cidades[coisas['Minas Gerais']])
for estado, abrev in list(coisas.items()):
    print(f'{estado} é abreviado por {abrev}')

for abrev, cidade in list(cidades.items()):
    print(f'{cidade} é uma cidade de {abrev}')

for estado, abrev in list(coisas.items()):
    print(f'{estado} é abreviado por {abrev}')
    print(f'e a cidade {cidades[abrev]}')