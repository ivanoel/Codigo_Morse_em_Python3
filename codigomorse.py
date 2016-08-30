#!/usr/bin/python
'__autor__' == '__Ivanoel__'

from winsound import Beep
from time import sleep

while 1:
    print ('Escolha a velocidade de tradução')
    print ('Rapido (1)')
    print ('Lento (2)')
    
    if int(input('Velocidade: ') == 1):
        vel = 0.4
    else:
        vel = 1
    texto = input('Texto a ser  traduzido (minusculo, sem acentos, Sair (fim)): ')
    if texto == 'fim':
        break

    morse={'m': '--',',': '--..--','1': '.----','0':'-----','3': '...--','2': '..---','5': '.....',
       '4': '....-','7': '--...','6': '-....','9': '----','8': '---..', '?': '..--..', 'a': '.-','c':
       '-.-.','b': '-...','e': '.', 'd': '-..', 'g': '--.', 'f': '..-.', 'i': '..', 'q': '--.-', 'p': '.--.',
       's': '...', 'r': '.-.', 'u': '..-', 't': '-', 'w': '.--', 'v': '...-', 'y': '-.--', 'x': '-..', 'z': '--..', '':'\n'}

    for i in texto:

        print(i, morse[i])

        for j in range(len(morse[i])):

            if morse[i][j] == '.':
                Beep(500,50*vel)
                sleep(0.1*vel)
            elif morse[i][j] == '-':
                Beep(500,150*vel)
                sleep(0.1*vel)
            else:
                sleep(0.3*vel)
        sleep(0.3*vel)
    input("enter para sair")