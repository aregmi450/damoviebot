#themovie moviebot
import tweepy as tp
import time
import os

# credentials to login twitter api

consumer_key = 'Insert consumer key code here'
consumer_secret = 'Insert consumer secret key code here'
access_token = 'Insert your access token key here'
access_secret = 'Insert your access secret key here'

#login to twitter account api:
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret )
api = tp.API(auth)

#iterates over pictures in movie folders

os.chdir('movies')
for movie_image in os.listdir('.'):
    api.update_with_media(movie_image, status="Here is a movie/series for you")
    time.sleep(1800) 
    #time after which the bot will repost 
