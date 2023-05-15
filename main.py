import tweepy
import api_keys
import cal

##########################
# Twitter API Management #
##########################

hashtags = "#holidays #usa #countdown"

client = tweepy.Client(
    consumer_key=api_keys.API_key,
    consumer_secret=api_keys.API_key_secret,
    access_token=api_keys.access_token,
    access_token_secret=api_keys.access_token_secret
)

def generate_msg():
    return f"🇺🇸 Holidays:\n{cal.remaining_days_result()}\n{hashtags}"


def main():
    msg = client.create_tweet(text=generate_msg())
    tweet_id = msg.data['id']

    client.create_tweet(in_reply_to_tweet_id=tweet_id,text="This tweet was made by a bot. See you tomorrow for the countdown.")


if __name__ == '__main__':
    main()