import tweepy
consumer_key = "******"
consumer_secret = "******"
access_key = "******"
access_secret = "******"



# Create an Api instance.
#submit key and secret.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search_users, q='League of Legends').items(8):
    print(tweet.screen_name)


# recent_tweet = api.user_timeline('YuhanCh71346999')
# for twee in recent_tweet:
#     print(twee.text)

#print me
me = api.me()
print("my id: ",me.id_str, "\nmy screen name: ",me.screen_name)


specific_user="@GenshinImpact"
# get user
user = api.get_user("@GenshinImpact")
print("\nUser id: ",user.id_str,"\nScreen Name: ",user.screen_name)

# User_timeline: Returns the 5 most recent statuses posted from the authenticating user or the user specified.
recent_tweet = api.user_timeline(user.id_str,count=5)
for tweet in recent_tweet:
    print('tweet id: ',tweet.id,'\ntweet text: ',tweet.text)

