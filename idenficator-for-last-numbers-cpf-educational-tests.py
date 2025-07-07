print('colque os nove primeiros dígitos de um cpf que os dois números identificadores serão revelados')
n1=int(input('1°: '))
n2=int(input('2°: '))
n3=int(input('3°: '))
n4=int(input('4°: '))
n5=int(input('5°: '))
n6=int(input('6°: '))
n7=int(input('7°: '))
n8=int(input('8°: '))
n9=int(input('9°: '))
i1=((n1*10+n2*9+n3*8+n4*7+n5*6+n6*5+n7*4+n8*3+n9*2)*10)%11
if i1>9:
        i1=0
i2=((n1*11+n2*10+n3*9+n4*8+n5*7+n6*6+n7*5+n8*4+n9*3+i1*2)*10)%11
if i2>9:
        i2=0
print(f'O CPF completo é: \033[1;40m{n1}{n2}{n3}.{n4}{n5}{n6}.{n7}{n8}{n9}-{i1}{i2}\033[0m')
