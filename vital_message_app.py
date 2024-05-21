import os
import string
from random import choice
from time import sleep

print("VITAL MESSAGE")

dificuldade = 0
while dificuldade < 4 or dificuldade > 10:
    dificuldade = int(input("Digite a dificuldade: "))

mensagem = ""
for _ in range(dificuldade):
    char = choice(string.ascii_letters)
    mensagem += char

print(mensagem)
sleep(1 * dificuldade)

print("\n" * 100)

mensagem_resposta = str(input("Digite a mensagem memorizada: "))
if mensagem_resposta == mensagem:
    print("MENSAGEM ESTÁ CORRETA! A GUERRA TERMINOU!")
else:
    print(f"VOCÊ ERROU, DEVERIA TER ENVIADO {mensagem}")
