n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1>n2 and n1>n3:
    print('O número {} é o maior entre os três'.format(n1))
if n2>n1 and n2>n3:
    print('O número {} é o maior entre os três'.format(n2))
if n3>n1 and n3>n2:
    print('O número {} é o maior entre os três'.format(n3))
if n1<n2 and n1<n3:
    print('O número {} é o menor entre os três'.format(n1))
if n2<n1 and n2<n3:
    print('O número {} é o menor entre os três'.format(n2))
if n3<n1 and n3<n2:
    print('O n[umero {} é o menor entre os três'.format(n3))