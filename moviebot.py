#themovie moviebot
import tweepy as tp
import time
import os

# credentials to login twitter api

consumer_key = '9OFeftgAAlW1qbmpeE3xGmfw2'
consumer_secret = 'gGAm87j8vFxtRNIPZJEcQB5CHUcsiQwjBtDszgsYxvCKGItKVw'
access_token = '1278599604947173377-P0dyNch0od5KOTPzbgZdqrgm8zToxW'
access_secret = 'iq294wBPeTa7UdUB4oc5IanccTlc90DBIDmGRnl36JuP0'

#login to twitter account api:
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret )
api = tp.API(auth)

#iterates over pictures in movie folders

os.chdir('movies')
for movie_image in os.listdir('.'):
    api.update_with_media(movie_image, status="Here is a movie/series for you")
    time.sleep(1800)
