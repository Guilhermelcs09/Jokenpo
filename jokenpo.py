from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('='*21)
print('  \033[31m     JOKENPO \033[m')
print('='*21)


print('''
[ 0 ] PARA JOGAR PEDRA
[ 1 ] PARA JOGAR PAPEL
[ 2 ] PARA JOGAR TESOURA''')


jogador = int(input('JOGUE: '))
print('='*21)
print('JO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PO')
print('='*21)

if computador == 0:
    if jogador == 0:
        print('\033[mEMPATE')
    elif jogador == 1:
        print('\033[32;1mVOCÊ GANHOU\033[m')
    elif jogador == 2:
        print('\033[32;1mCOMPUTADOR GANHOU!!\033[m')

elif computador == 1:
    if jogador == 2:
        print('\033[32;1mVOCÊ GANHOU')
    elif jogador == 0:
        print('\033[31;1mCOMPUTADOR GANHOU!!\033[m')
    elif jogador == 1:
        print('EMPATE')

elif computador == 2:
    if jogador == 0:
        print('\033[32;1mVOCÊ GANHOU\033[m')
    elif jogador == 1:
        print('\033[31;1mCOMPUTADOR GANHOU!!\033[m')
    elif jogador == 2:
        print('EMPATE')

print('\033[33;1mO COMPUTADOR JOGOU {}\033[m'.format(itens[computador]))
