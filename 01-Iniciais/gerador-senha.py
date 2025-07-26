import random
import string
print('\033[7;4;1mGERADOR DE SENHAS ALEATÓRIAS\033[0m')
a=random.choices(string.ascii_letters,k=4)
n=random.choices(string.digits, k=4)
cc=input('A senha precisa de caracteres especiais?\033[4;32m(sim)\033[0m ou \033[4;31m(não)\033[0m: ').strip().lower()
if cc=='sim':
    c=random.choices(string.punctuation, k=2)
    l=c+a+n
    random.shuffle(l)
    s=''.join(l)
    print(f'A sua senha é:\033[4;35m{s}\033[0m')
elif cc=='não' or cc=='nao':
    l=[a,n]
    random.shuffle(l)
    s = ''.join(l)
    print(f'A senha aleátória é: \033[4;32m{s}\033[0m')