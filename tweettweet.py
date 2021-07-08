import tweepy
import time

consumer_key = 'YSiiIRTe0poG7CNyXBQeRu96w'
consumer_secret = '5S9hHgQsCDwrePKPj8KyaZObQsO84O3VWyYjhaeNSSTVXJFZyL'
access_token = '862738332-6nkB4hcFJDKjUbHV3LDk4mrEY4EJfbPujDy5zQmk'
access_token_secret = 'fttyFJ3P4UlBQ27i0LAREkDLitBot4jbdIUHfuHJDXNn5'

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
        time.sleep(300)



search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# #Generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Shivani':
#         follower.follow()
#         break