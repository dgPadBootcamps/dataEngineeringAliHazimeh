import twitter
import json
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
qr = "(lebanon or لبنان) since:" + str(yesterday) + " until:" + str(today)

scraper = twitter.TwitterSearchScraper(qr, False)

tweets = []

for i, tweet in enumerate(scraper.get_items()):
    # if i > 5:
    #     break
    # data retrieve from tweet_to_tweet class in the twitter.py file
    tweets.append(
        {"id": tweet.id,
         "Full Text": tweet.content,
         "Tweet Date": str(tweet.date),
         "List Of #": tweet.hashtags if tweet.hashtags is not None else [],
         "List Of Mentions": tweet.mentionedUsers if tweet.mentionedUsers is not None else [],
         "User": {"Username": tweet.user.username,
                  "Display": tweet.user.displayname,
                  "Descriptions": tweet.user.description,
                  "Followers": tweet.user.followersCount,
                  "Following": tweet.user.friendsCount,
                  "User Id": str(tweet.user.id),
                  "Website URL": tweet.user.linkUrl,
                  "Is verified": tweet.user.verified,
                  "Status Count": tweet.user.statusesCount,
                  "Joined Date": str(tweet.user.created),
                  "Locations": tweet.user.location},
         "Is Retweet": tweet.retweetedTweet,
         "Retweet Count": tweet.retweetCount,
         "Is Reply": (tweet.retweetCount != None),
         "Quote Count": tweet.quoteCount,
         "replyCount": tweet.replyCount,
         "Lang": tweet.lang,
         "has media": tweet.media is not None,
         "Favorite": tweet.likeCount,
         "Tweet Location": tweet.place})

# to write all fetched data into json file tweets.json
with open("date.json", "w", encoding="utf-8") as file:
    json.dump(tweets, file, ensure_ascii=False, indent=4)
