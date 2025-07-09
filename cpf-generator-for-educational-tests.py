print('\033[4;33mEle gera CPFs com estrutura válida, mas que não pertencem a pessoas reais.\033[0m')
print(
    '\033[4;31mNÃO\033[0m \033[4;33mutilize os CPFs gerados para qualquer tipo de cadastro real ou atividade ilegal.\033[0m')
print('\033[4;33mO autor não se responsabiliza por usos indevidos.\033[0m')
from random import randint

a = input('Gerar um CPF ?(digite \033[4;32msim\033[0m ou \033[4;31mnão\033[0m): ').lower().strip()
if a == 'sim':
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
elif a == 'não' or a == 'nao':
    print('Ok.')
else:
    print('Desculpe, não entendi sua resposta, tente novamente.')

