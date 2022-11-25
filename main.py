from ler_csv import ler_utilizadores
from menus import menu0, menu1,menu2, menu3
from switch_case_twitter import escrever_utilizadores, switch_twitter
from utilizador import Utilizador


def criar_conta(ultimo_numero):
    handle_check = False
    lista_de_handles = [ user.handle for user in Utilizador.lista_utilizadores ]
    handle = ""
    while not handle_check:
        handle = str(input('\nIntroduza o novo Handle com o "@" no inicio: '))
        if handle not in lista_de_handles and handle.startswith('@'):
            handle_check = True
        else:
            print('\nUtilizador já existe ou esqueceu-se do "@". ')
    nome_completo = str(input('\nIntroduza o seu nome completo: '))
    password = str(input('\nIntroduza a sua password: '))
    descricao = str(input('\nIntroduza a sua descrição: '))
    numero = str(ultimo_numero)
    novo_utilizador = Utilizador(handle, password, numero, nome_completo, descricao)
    escrever_utilizadores()

user = ""
resposta_user = False
while not resposta_user: 

    ler_utilizadores()
    menu0()
    
    ultimo_numero = int(Utilizador.lista_utilizadores[len(Utilizador.lista_utilizadores)-1].numero)+1

    criar_conta_nova = str(input('Já tem uma conta do Twitter? "s" para sim "n" para não: '))
    
    if criar_conta_nova == 'n':
        criar_conta(ultimo_numero)

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