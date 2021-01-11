import tweepy
import json

file = open("keys.txt","r")
dict_keys = {}
elem = []
for line in file:
    elem = line.split("=")
    dict_keys[elem[0]] = elem[1].rstrip('\n')
    print(elem)
auth = tweepy.OAuthHandler(dict_keys.get("consumer_key"),dict_keys.get("consumer_secret"))
auth.set_access_token(dict_keys.get("Access_token"),dict_keys.get("Access_token_secret"))


api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True) # Si llega al limite de cupo, el programa no va a crashear sino que espera a que haya cupo otra vez
#MI PROPIA INFORMACION

data = api.me() 
#Data -> Es un objeto 'User'
print(json.dumps(data._json,indent=2)) 

#Todo objeto 'User' tiene el atributo ._json que devuelve el json de los datos 
#Espacio para visualizar el JSON 

#INFORMACION DE OTRO USUARIO 

#data = api.get_user("nike")
#print(json.dumps(data._json,indent=2))

#OBTENER FOLLOWERS DE UN USUARIO  
#data = api.followers(screen_name="nike") #-> entrega resultados paginados, datos en grupos 

#OBTENER FOLLOWERS EVITANDO PAGINACION 

# Con esta clase (utilidad) de tweepy se pueden obtener la cantidad que se quiera de los que se quiera de twitter
#Parametros: 1. Metodo (sin la llamada), 2. Usuario (nombre del arroba), 3. Cuantos items se quieren obtener

#for user in tweepy.Cursor(api.friends,screen_name="nike").items(100):
#    print(json.dumps(user._json,indent=2))

#OBTENER UN TIMELINE -> TODOS LOS TWEETS DE UN USUARIO

#for tweet in tweepy.Cursor(api.user_timeline,screen_name="mauriciodavidc",tweet_mode = "extended").items(2):
#    data = json.dumps(tweet._json,indent = 2)
#    print(dict(data))
# El parametro 3 del Cursor indica la longitud del tweet dado que en algun momento fue cambiado 

#BUSCAR TWEETS 

#for tweet in tweepy.Cursor(api.search,q="vaticano",tweet_mode="extended").items(5): 
#    print(json.dumps(tweet._json,indent=2))

#Mas informacion en https://tweepy.readthedocs.io/en/v3.5.0/