import os
from time import sleep

def limpar_tela():
    # Verifica qual o sistema operacional para executar o comando correto de limpeza
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux, macOS e outros sistemas
        os.system('clear')

# Exemplo de uso
print("Texto antes de limpar a tela.")
sleep(3)
limpar_tela()
print("Texto após limpar a tela.")