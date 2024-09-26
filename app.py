#laço de repeticao
#import as bibliotecas inclusive a os e time
#tras os prompts de comandos do windows e di linux tambémn e se quiser posso desligar o pc

import os
import time
n = int(input("informe um numero inteiro positivo: "))
while n >= 0:
    os.system("cls")
    print(n)
    time.sleep(1)
    n -= 1
os.system("cls") #limpa a tela se for o linux e clear
print("boom")
#para interromper o loop ctrl+c
# so vai funcionar se a condicional for verdadeira
