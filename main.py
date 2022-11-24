from ler_csv import ler_utilizadores
from menus import menu1,menu2, menu3
from switch_case_twitter import switch_twitter
from utilizador import Utilizador

user = ""
resposta_user = False
while not resposta_user: 

    ler_utilizadores()
    menu1()

    handle = str(input('Introduza o seu handle: '))
    password = str(input('Introduza a sua password: '))

    verificacao = Utilizador.verfificar_user(handle, password)

    if verificacao[0] == False:
        print('Utilizador não existe ou Password Incorreta')
        resposta_user = verificacao[0]
    else:
        resposta_user = verificacao[0]
        user = verificacao[1]
        
menu2()

opcao = True
while opcao:
    menu3()
    selecao = int(input('Digite a sua opcao: '))
    switch_twitter(selecao, user)