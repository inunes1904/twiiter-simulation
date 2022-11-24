import pandas
from utilizador import Utilizador

def ler_utilizadores():
    users = pandas.read_csv('users_file/users.csv', sep=';')
    for i, user in users.iterrows():
        novo_utilizador = Utilizador(handle=user['Handle'],
                                     numero=user['Numero'],
                                     nome_completo=user['Nome_Completo'],
                                     descricao=user['Descricao'],
                                     password=user['Password'])
    
        
        