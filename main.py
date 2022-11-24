from ler_csv import ler_utilizadores
from menus import menu1,menu2, menu3
from switch_case import switch
from utilizador import Utilizador

user = ""
answer = False
while not answer: 

    ler_utilizadores()
    menu1()

    handle = input('Introduza o seu handle:')
    password = input('Introduza a sua password:')

    answer, user = Utilizador.verfificar_user(handle, password)
    if not answer:
        print('Utilizador não existe ou Password Incorreta')

menu2()

opcao = True
while opcao:
    menu3()
    selecao = int(input('Digite a sua opcao: '))
    switch(selecao, user)