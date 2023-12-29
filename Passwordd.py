import random

parole = 'abcdefghijklmnopqrstuvwxyz'
numeri = '1234567890'
caratteri = '&!-_$*/-+%£=?,<>'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def weak():
    parola_scelta = [random.choice(parole) for _ in range(4)]
    numeri_scelto = [random.choice(numeri) for _ in range(2)]
    caratteri_scelti = [random.choice(caratteri) for _ in range(2)]
    uppercase_scelta = [random.choice(uppercase) for _ in range(2)]

    array = list(zip(parola_scelta, numeri_scelto, caratteri_scelti, uppercase_scelta))

    random.shuffle(array)

    password_str = ''.join(''.join(t) for t in array)

    print("Password:", password_str)

def medium():
    parola_scelta = [random.choice(parole) for _ in range(6)]
    numeri_scelto = [random.choice(numeri) for _ in range(3)]
    caratteri_scelti = [random.choice(caratteri) for _ in range(4)]
    uppercase_scelta = [random.choice(uppercase) for _ in range(4)]

    array = list(zip(parola_scelta, numeri_scelto, caratteri_scelti, uppercase_scelta))

    random.shuffle(array)

    password_str = ''.join(''.join(t) for t in array)

    print("Password:", password_str)

def strong():
    parola_scelta = [random.choice(parole) for _ in range(6)]
    numeri_scelto = [random.choice(numeri) for _ in range(6)]
    caratteri_scelti = [random.choice(caratteri) for _ in range(5)]
    uppercase_scelta = [random.choice(uppercase) for _ in range(4)]

    array = list(zip(parola_scelta, numeri_scelto, caratteri_scelti, uppercase_scelta))

    random.shuffle(array)

    password_str = ''.join(''.join(t) for t in array)

    print("Password:", password_str)

scelta = 4

while scelta != 1 and scelta != 2 and scelta != 3:
    scelta = int(input("1:Weak, 2:Medium, 3:Strong: "))

    if scelta == 1:
        password = weak()
    elif scelta == 2:
        password = medium()
    elif scelta == 3:
        password = strong()
    else:
        print('Invalid selection')