import tweepy
import time

consumer_key = 'YSiiIRTe0poG7CNyXBQeRu96w'
consumer_secret = '5S9hHgQsCDwrePKPj8KyaZObQsO84O3VWyYjhaeNSSTVXJFZyL'
access_token = '862738332-lCGcx3y0zfneT91jrjpQJ8XuIBHRvSNE0dhqgty8'
access_token_secret = 'RpqSvQTdiQcpvAIGACHRUdNhrjApWCs7iJxahJBUbmErL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.followers_count)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

#Generous bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)