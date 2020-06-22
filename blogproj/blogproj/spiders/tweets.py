# # -*- coding: utf-8 -*-
# import scrapy
# import json


# class TweetsSpider(scrapy.Spider):
#     name = 'tweets'
#     allowed_domains = ['http://www.trumptwitterarchive.com/archive']
#     start_urls = [
#     	'http://www.trumptwitterarchive.com/data/realdonaldtrump/2020.json'
#     	]
#     def parse(self, response):
# 		jsonresponse = json.loads(response.body)

# 	    for tweet in jsonresponse:
# 	        yield {'created_at': tweet['created_at'],
# 	               'favorite_count': tweet['favorite_count'],
# 	               'id_str': tweet['id_str'],
# 	               'in_reply_to_user_id_str': tweet['in_reply_to_user_id_str'],
# 	               'is_retweet': tweet['is_retweet'],
# 	               'retweet_count': tweet['retweet_count'],
# 	               'source': tweet['source'],
# 	               'text': tweet['text']}

#     # def parse(self, response):
#     # 	jsonresponse = json.loads(response.body)

#     	# for tweet in jsonresponse:
#     	# 	yield {"created_at": tweet['created_at'],
#     	# 			"retweet_count": tweet['retweet_count'],
#     	# 			"in_reply_to_user_id_str": tweet['in_reply_to_user_id_str'], 
# 					# "favorite_count": tweet['favorite_count'], 
# 					# "is_retweet": tweet['is_retweet'],
# 					# "source": tweet['source'],
# 					# "text": tweet['text'],}