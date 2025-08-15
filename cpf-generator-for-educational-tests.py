print('''⚠️ \033[4;31mAVISO LEGAL:\033[0m
\033[4;33mEste código tem o objetivo apenas educacional e para testes de software.
Ele gera CPFs com estrutura válida, mas que não pertencem a pessoas reais.\033[0m
\033[4;31mNÃO\033[0m \033[4;33mutilize os CPFs gerados para qualquer tipo de cadastro real ou atividade ilegal.
O autor não se responsabiliza por usos indevidos.\033[0m''')
from random import randint
from time import sleep
a = input('Gerar um CPF ?(digite \033[4;32msim\033[0m ou \033[4;31mnão\033[0m): ').lower().strip()
while a!='sim' and a!='não' and a!='nao':
    print('não entendi sua resposta, tente novamente...')
    a=input('\033[1;4;32m(sim)\033[0m ou \033[1;4;31m(não)\033[0m: ')
if a == 'sim':
    while True:
        r = input('E qual será a região do CPF? ').lower().strip()
        regioes= {
                1: ['distrito federal', 'goias', 'mato grosso do sul','tocantins'],
                2: ['acre','amazonas','amapa','rondonia','roraima','para'],
                3: ['ceara','maranhao','piaui'],
                4: ['alagoas','pernambuco','paraiba','rondonia'],
                5: ['bahia','sergipe'],
                6: ['minas gerais'],
                7: ['Espirito Santo','rio de janeiro'],
                8: ['sao paulo'],
                9: ['parana','santa catarina'],
                0: ['rio grande do sul']
        }

        n9 = None
        for e, est in regioes.items():
            if r in est:
                n9=e
                break
        if n9 is None:
            print('\033[4;31mDesculpe, não entendi sua resposta, tentenovamente sem pontos de acentuação.\033[0m')
        else:
            n1 = randint(0, 9)
            n2 = randint(0, 9)
            n3 = randint(0, 9)
            n4 = randint(0, 9)
            n5 = randint(0, 9)
            n6 = randint(0, 9)
            n7 = randint(0, 9)
            n8 = randint(0, 9)
            i1 = ((n1 * 10 + n2 * 9 + n3 * 8 + n4 * 7 + n5 * 6 + n6 * 5 + n7 * 4 + n8 * 3 + n9 * 2) * 10) % 11
            if i1 > 9:
                i1 = 0
            i2 = ((n1 * 11 + n2 * 10 + n3 * 9 + n4 * 8 + n5 * 7 + n6 * 6 + n7 * 5 + n8 * 4 + n9 * 3 + i1 * 2) * 10) % 11
            if i2 > 9:
                i2 = 0
            CPF = f'{n1}{n2}{n3}.{n4}{n5}{n6}.{n7}{n8}{n9}-{i1}{i2}'
            print(f'\033[35mO CPF gerado foi:\033[0m \033[4;32m|{CPF}|\033[0m')
            sleep(1)
        reiniciar = input("\033[1;35mDigite 'R' para reiniciar o gerador, ou 'N' para parar: \033[0m").strip().lower()
        if reiniciar == 'r':
            print("\033[1;35mreiniciando...\033[0m")
            sleep(1)
        elif reiniciar == 'n':
            print("\033[1;31mEncerrando...\033[0m")
            sleep(1)
            break
elif a == 'não' or a == 'nao':
        print('Ok.')
else:
        print('Desculpe, não entendi sua resposta, tente novamente.')

