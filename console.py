from datetime import date, timedelta

from data_collection import scraper

today = date.today()
yesterday = today - timedelta(days=1)
qr = "(lebanon OR لبنان) since:" + str(yesterday) + " until:" + str(today)

tweets = scraper.search(qr)
