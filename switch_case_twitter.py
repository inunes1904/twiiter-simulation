import json
from datetime import date, datetime

from utilizador import Utilizador

# escrever users
def escrever_utilizadores():
    with open('users_file/users.csv', 'w') as ficheiro_users:
                    ficheiro_users.write('Numero;Handle;Nome_Completo;Descricao;Password'+'\n')
                    for user in Utilizador.lista_utilizadores:
                        ficheiro_users.write(f'{user.numero};{user.handle};{user.nome_completo};{user.descricao};{user.password}'+'\n')

# ler tweets do ficheiro Json
def ler_tweets():
    with open('tweets_file/tweets.json', 'r') as json_file:
        tweets = json.load(json_file)
    return tweets

# escrever tweetd no ficheiro
def escrever_tweets(tweets):
    with open('tweets_file/tweets.json', "w") as ficheiro:
        json.dump(tweets, ficheiro)

# mostrar tweets do utilizador
def mostrar_tweets(user_tweets):
    print('\n\nOs meus tweets ordenados por data:\n__________________________________\n')
    if user_tweets:
        for tws in user_tweets:
            for key, tweet in tws.items():
                print('{} : {}'.format(key, tweet))
            print('\n-----------------------------------------------\n')
    else:
        print('Não possui tweets na paltaforma experimente a opção Adicionar Tweet\n\n')
        

# retorn tweets por data do utilizador logado
def filtrar_tweets_user(tweets, user):
    user_tweets = []          
    for tweet in tweets['tweets']:
        if user.handle == tweet['handle']:
            user_tweets.append(tweet)
    user_tweets = sorted(user_tweets, key=lambda d: d['data'], reverse=True)
    return user_tweets
    

def switch_twitter(selecao, user):
    match selecao:
        # Listagem dos meus tweets
        case 1:   
            tweets = ler_tweets()
            user_tweets = filtrar_tweets_user(tweets, user)   
            mostrar_tweets(user_tweets)
        # Adicionar Tweet
        case 2:
            tweets = ler_tweets()
            texto = input('Introduza o texto do tweet: ') 
            visibilidade = input('Digite Pub para Publico ou Priv Privado:').lower()
            if visibilidade == 'pub':
                visibilidade = 'Publico'
            else:
                visibilidade = 'Privado'
            handle = user.handle
            data =  datetime.now().strftime("%d-%m-%Y %H:%M")
            nr_tweets = len(tweets['tweets'])
            id_tweet = int(tweets['tweets'][nr_tweets-1]['id'])+1
            
            novo_tweet = {
                  "id": id_tweet,
                  "texto":texto,
                  "visibilidade":visibilidade,
                  "data":str(data),
                  "handle":handle
            }
            tweets['tweets'].append(novo_tweet)
            escrever_tweets(tweets)
        case 3:
            tweets = ler_tweets()
            user_tweets = filtrar_tweets_user(tweets, user)
            mostrar_tweets(user_tweets)
            id = int(input('Insira o id do Tweet que deseja eliminar: '))
            tweets['tweets'] = [ tw for tw in tweets['tweets'] if  tw['id'] != id]
            escrever_tweets(tweets)
            print('Tweet removido com sucesso.\n')
        case 4:
            print('\n_______________________________________________________________________\n')
            handle = str(input('\n\nDeseja alterar o seu Handle? "s" para sim "n" para não: '))
            if handle == 's':
                handle = str(input('Introduza o novo Handle com o "@" no inicio: '))
                tweets = ler_tweets()
                for tw in tweets['tweets']:
                    for k, v in tw.items():
                        if k == 'handle' and v == user.handle:
                           tw['handle'] = handle    
                user.handle = handle
                escrever_tweets(tweets)
            print('\n_______________________________________________________________________\n')
            password = str(input('\n\nDeseja alterar a sua password? "s" para sim "n" para não: '))
            if password == 's':
                password = str(input('Introduza a sua nova password: ')) 
                user.password = password
            print('\n_______________________________________________________________________\n')
            nome_completo = str(input('\n\nDeseja alterar o seu Nome? "s" para sim "n" para não: '))
            if nome_completo == 's':
                nome_completo = str(input('Introduza o seu novo Nome: ')) 
                user.nome_completo = nome_completo
            print('\n_______________________________________________________________________\n')
            descricao = str(input('\n\nDeseja alterar a sua Descrição? "s" para sim "n" para não: '))
            if descricao == 's':
                descricao = str(input('Introduza a sua nova Descrição: ')) 
                user.descricao = descricao
            escrever_utilizadores()
            print('\n_______________________________________________________________________\n\n')
            print('Utilizador modificado com sucesso...\n\n')
        case 5:
            print('Tem a certeza que deseja eliminar a sua conta?\n')
            print('Todos os seus Tweets e informação será removida\n')
            decisao = input('Digite "s" para eliminar a conta "n" para cancelar: ').lower()
            if decisao == 's':
                tweets['tweets'] = [ tw for tw in tweets['tweets'] if  tw['handle'] != user.handle]
                escrever_tweets(tweets)
                if user:
                    Utilizador.lista_utilizadores.remove(user)
                escrever_utilizadores()
                print('\n\n_________________________________________________\n\n')
                print('Sua conta foi eliminada com sucesso, volte sempre!')
                exit(1)
        case 0:
            print('\n\nAté á próxima volte sempre...')
            exit()