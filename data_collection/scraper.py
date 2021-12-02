from data_collection import twitter
import json


def search(query):
    scraper = twitter.TwitterSearchScraper(query, False)

    tweets = []

    for i, tweet in enumerate(scraper.get_items()):
        # if i > 1000:
        #     break
        # data retrieve from tweet_to_tweet class in the twitter.py file
        print(tweet.id)
        tweets.append(
            {"id": tweet.id,
             "full_text": tweet.content,
             "tweet_date": str(tweet.date),
             "list_of_mention": tweet.hashtags if tweet.hashtags is not None else [],
             "mentions": [x.displayname for x in tweet.mentionedUsers] if tweet.mentionedUsers is not None else [],
             # "user": {"username": tweet.user.username,
             #          "display": tweet.user.displayname,
             #          "descriptions": tweet.user.description,
             #          "followers": tweet.user.followersCount,
             #          "following": tweet.user.friendsCount,
             #          "user_id": str(tweet.user.id),
             #          "url": tweet.user.linkUrl,
             #          "is_verified": tweet.user.verified,
             #          "status_count": tweet.user.statusesCount,
             #          "joined_date": str(tweet.user.created),
             #          "location": tweet.user.location},
             "username": tweet.user.username,
             "display": tweet.user.displayname,
             "descriptions": tweet.user.description,
             "followers": tweet.user.followersCount,
             "following": tweet.user.friendsCount,
             "user_id": str(tweet.user.id),
             "url": tweet.user.linkUrl,
             "is_verified": tweet.user.verified,
             "status_count": tweet.user.statusesCount,
             "joined_date": str(tweet.user.created),
             "location": tweet.user.location,
             "is_retweet": tweet.retweetedTweet,
             "retweet_count": tweet.retweetCount,
             "is_reply": (tweet.retweetCount is not None),
             "quote_count": tweet.quoteCount,
             "reply_count": tweet.replyCount,
             "language": tweet.lang,
             "has_media": tweet.media is not None,
             "like_count": tweet.likeCount,
             "tweet_location": str(tweet.place)})

    return tweets


def save_json(tweets, today):
    # to write all fetched data into json file tweets.json
    file_storage = "D:\dgPad\data_storage\Twitter-Lebanon-" + str(today) + ".json"
    with open(file_storage, "w", encoding="utf-8") as file:
        json.dump(tweets, file, ensure_ascii=False, indent=4)
    print("Great :)")
