import twitter
import json

scraper = twitter.TwitterUserScraper("BillGates", False)

tweets = []

# i means the index and tweet means that we are getting in
# this function give me all the tweet to limit the number we create if conditions for the index latest 3 tweet
for i, tweet in enumerate(scraper.get_items()):
    if i > 20:
        break
    # data retrieve from tweet_to_tweet class in the twitter.py file
    tweets.append(
        {"url": tweet.url, "id": tweet.id, "content": tweet.content, "likeCount": tweet.likeCount,
         "replyCount": tweet.replyCount})
# to write all fetched data into json file tweets.json
with open("tweets.json", "w", encoding="utf-8") as file:
    json.dump(tweets, file, ensure_ascii=False, indent=4)
# testing push and commit on github