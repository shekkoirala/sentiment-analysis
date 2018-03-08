from .sentimentAnalysis import sentiment
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from models import LiveSentiment, Sentiment

#consumer key, consumer secret, access token, access secret.
ckey="oSJ0d8UPjA9ISET5T0fulouKx"
csecret="Du8ByoBskIKmN0XpXNM6NuDo1b67EdE5jnmz5dZIANAMoPzAZc"
atoken="125867357-oylJjj1fS82s9OLsfRZ07MujS6QIhyeVjSdOSnqW"
asecret="FFARkx5rXrJZTwfAnXEmSwU4EJq3KWrcoNbh7INfTPhp2"

liveSentiment = LiveSentiment("liveSentiment")
tweetSentiment = Sentiment("sentiment")

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 50:
            if sentiment_value == "pos":
                print ("POS")
                liveSentiment.pos += 1
                tweetSentiment.pos += 1
            elif sentiment_value == "neg":
                print ("NEG")
                liveSentiment.neg += 1
                tweetSentiment.neg += 1

            liveSentiment.update_in_database()
            tweetSentiment.update_in_database()

        # output = open("twitter-out.txt","a")
        # output.write(sentiment_value)
        # output.write('\n')
        # output.close()

        return True

    def on_error(self, status):
         app.logger.info("Error! %", (status))


def stream(tag):
    # tag must be a string
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    liveSentiment.tag = tag
    tweetSentiment.tag = tag

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[tag])