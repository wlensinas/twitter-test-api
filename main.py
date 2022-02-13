import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(f'Date: {str(tweet.created_at)}')
        print(f'Content: {tweet.text}')
        print(f'Where: {tweet.coordinates}')
        print('------------------------------')
        print('------------------------------')
    # print(api.verify_credentials().screen_name)
except tweepy.errors.TweepyException as e:
    print('Twitter Error')
    print(e)
except Exception as e:
    print('General Exception')
    print(e)

