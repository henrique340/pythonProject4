nt = int(input('digite um termo: '))#primeiro termo
nr = int(input('digite a razão: '))
dec = nt + (10   - 1) * nr           #decimo termo
for c in range(nt, dec+nr, nr):
    print('{}'.format(c), end='->')
print('FIM')