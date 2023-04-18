def notas(*num,sit=False):
    """
    --> função para analisar notas
    :param num:  notas dos alunos
    :param sit: (opcional) se True então mostra as situações da média
    :return: dicionário com a informação das notas
    """
    dado = dict()
    dado['total'] = len(num)
    dado['maior'] = max(num)
    dado['menor'] = min(num)
    dado['média'] = sum(num)/len(num)
    if sit:
        if dado['média'] >= 7:
            dado['situação'] = 'boa'
        elif dado['média'] >= 5:
            dado['situaçãõ'] = 'razoável'
        else:
            dado['situção'] = 'ruim'
    return dado


#programa principal
resposta = notas(5.5, 2.5, 8.0, 9.0, sit=True)
print(resposta)
help(notas)