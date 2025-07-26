from datetime import datetime
from time import sleep
while True:
    print('\033[1;33;4m-=-\033[0m'*18)
    print(f'\033[1m{'-'*10}CALCULADORA DE ANOS BISSEXTOS{'-'*10}')
    print('\033[1;33;4m-=-\033[0m' * 18)
    y=input('Digite o ano que você está \033[1;35mOU\033[0m aperte \033[1;33mENTER\033[0m para calcular automaticamente: ')
    print('\033[1;35m Processando...\033[0m')
    sleep(2)
    if y.strip()=='':
        y2=datetime.now().strftime('%Y')
        if int(y2)%4>0:
            print(f'Ao analisar o ano que seu computador está, eu conlui que seu ano \033[1;33mNÃO é BISSEXTO.\033[0m')
        elif int(y2)%4==0 and int(y2)%100>0 or int(y2)%400==0:
            print('ao analisar a data do seu computador, eu conclui que seu ano é \033[32mBISSEXTO\033[0m.')
    else:
        if int(y) % 4 == 0 and int(y) % 100 > 0 or int(y) % 400 == 0:
            print('O ano digitado é \033[1;35mBISSEXTO.')
        elif int(y)%4>0 or int(y)%100==0:
            print('O ano Digitado \033[1;31mNÃO\033[0m é \033[1;35mBISSEXTO\033[0m.')
    reiniciar=input('''\033[1;7;32maperte ENTER caso queira reiniciar o código, ou digite '1' caso queira encerrar\033[0m: ''')
    if reiniciar.strip()=='':
        print('\033[1;32m Reiniciando...\033[0m')
        sleep(2)
    elif reiniciar.strip()=='1':
        break