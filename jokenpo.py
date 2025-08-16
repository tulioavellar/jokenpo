#Libraries that helps to randomize the code's option in each game
from random import randint
from time import sleep

#list with option the code can choose

opt = ['pedra', 'papel', 'tesoura'] 
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
choice = int(input('Qual é a sua jogada? ')) #player's selection

#tiny animation before results, with a little delay in each phrase

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-=' * 11)

#main part of the code, which analyzes the outputs

if choice > 2:
    print('Escolha uma opção válida.')
    print('-=' * 11)
else:
    comp = randint(0, 2)
    print('Computador jogou {}.'.format(opt[comp]))
    print('Jogador jogou {}.'.format(opt[choice]))
    print('-=' * 11)
    if choice == comp:
        print('EMPATE')
    elif choice == 0 and comp == 1:
        print('COMPUTADOR VENCE')
    elif choice == 0 and comp == 2:
        print('JOGADOR VENCE')
    elif choice == 1 and comp ==  0:
        print('JOGADOR VENCE')
    elif choice == 1 and comp == 2:
        print('COMPUTADOR VENCE')
    elif choice == 2 and comp == 0:
        print('COMPUTADOR VENCE')
    elif choice == 2 and comp == 1:
        print('JOGADOR VENCE')
