import random
import os

def input_number(message):
    while True:
        try:
           user_input = int(input(message))
        except ValueError:
            print('Digite um Numero! tente novamente.')
            continue
        else:
            return user_input
            break   

def gerador_de_numeros():
        number = random.randint(1,100)
        return number
def display_gerando_numeros():
    print('foi gerado um numero de 1 a 100...')

input('Aperte enter para comecar...')
display_gerando_numeros()
message = 'Chute um numero de 1 a 100: '
jogar_novamente = 's'
number = gerador_de_numeros()
while jogar_novamente == 's':
    user_input = input_number(message)
    if user_input > number:
        print('Chute um numero menor')
    elif user_input < number:
        print('Chute um numero maior')
    else:
        print(f'PARABENS VOCE CHUTOU O VALOR CERTO: {user_input}')
        jogar_novamente = input('Jogo encerrado, gostaria de jogar novamenete?(s/n) ')
        if jogar_novamente == 's':
            os.system('cls')
            display_gerando_numeros()
            number = gerador_de_numeros()
            continue

print('---------------------------')
print('Encerrando o jogo...')
print('---------------------------')
