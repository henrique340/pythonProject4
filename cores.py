nome = 'yuji'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'brancopreto':'\033[7;30m'}

print('olá {}{}{}'.format(cores['brancopreto'], nome, cores['limpa']))
