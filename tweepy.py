import tweepy
import wget
import time
consumer_key ="PnJoznWHPHUGtD5t4nBtHC3eM"
consumer_secret = "XMeeRICVPnQN4NxKKq2ZbVRk5N7BEnn0xETmeCL0wfmNwaz8g9"
key = "1200760875524608000-nxTrFl8ViRnTTrGOmvip2TmdvYLG7A"
secret  ="W1aDHCxn4PId6eplQpB9F8zq2HqtfrTcCm7rSyRIWR3pS"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
#api.update_status('SECOND Tweet from Bot')


FILE_NAME = "last.txt"


def readd(FILE_NAME):
    file = open(FILE_NAME,'r')
    id2 = int(file.read().strip())
    file.close()
    return id2


def last_seen(FILE_NAME,id2):
    file = open(FILE_NAME,'w')
    file.write(str(id2))
    file.close()
    return


def reply():
    tweets = api.mentions_timeline(readd(FILE_NAME),tweet_mode = 'extended')
    media_files = set()
    global media
    for status in tweets:
        media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
        for media_file in media_files:
            wget.download(media_file)
    for tweet in reversed(tweets):
        if '#chandigarhpolice' or '#crime' or '#pcr' in tweet.full_text.lower():
            print("replied to " + str(tweet.id))

            api.update_status("@" + tweet.user.screen_name + " Thank you for Informing us. We will look in the following Request ",tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            last_seen(FILE_NAME,tweet.id)


while True:
    reply()

    time.sleep(60)
    print("Working.....")