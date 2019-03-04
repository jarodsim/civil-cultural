# -*- coding: utf-8 -*-

import tweepy

auth = tweepy.OAuthHandler('njdxGAN3jmlNb6tHmJQKjsxlx','ovrZM6KPZzFs5b5p5aErfLzl5TXWj6vC8eL5epQyiUEAxtUZJg')
auth.set_access_token('1053210512534708225-LmdiT80cDkFleze44PcUF7fdXHYSTw', 'ycFv8SEUGWKisVnEIyAOKNBNxpqB0McnhItwV2KlGGOue')

api = tweepy.API(auth)

results = api.search(q='Os vingadores', count = 10)

for result in results:
    print(result.text)
