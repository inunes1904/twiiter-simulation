import json
from datetime import date, datetime

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
    for tws in user_tweets:
        for key, tweet in tws.items():
            print('{} : {}'.format(key, tweet))
        print('\n-----------------------------------------------\n')

# retorn tweets por data do utilizador logado
def filtrar_tweets_user(tweets, user):
    user_tweets = []          
    for tweet in tweets['tweets']:
        if user.handle == tweet['handle']:
            user_tweets.append(tweet)
    user_tweets = sorted(user_tweets, key=lambda d: d['data'], reverse=True)
    return user_tweets
    

def switch(selecao, user):
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
        case 0:
            print('\n\nAté á próxima volte sempre...')
            exit()