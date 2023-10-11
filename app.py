import random
import os

input('Aperte enter para comecar...')

print('for gerado um numero de 1 a 100...')
number = random.randint(1,100)

jogar_novamente = 's'
while jogar_novamente == 's':
    user_input = int(input('Chute um numero de 1 a 100: '))
    if user_input > number:
        print('Chute um numero menor')
    elif user_input < number:
        print('Chute um numero maior')
    else:
        print(f'PARABENS VOCE CHUTOU O VALOR CERTO: {user_input}')
        jogar_novamente = input('Jogo encerrado, gostaria de jogar novamenete?(s/n) ')
        if jogar_novamente == 's':
            os.system('cls')
            print('for gerado um numero de 1 a 100...')
            number = random.randint(1,100)

print('---------------------------')
print('Encerrando o jogo...')
print('---------------------------')
