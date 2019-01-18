# import twitter
# import requests
# import re
# import random
#
# text_archive = ""
#
# api = twitter.Api(consumer_key = 'tjxBVZS2Xu2ay4VKlLqB0bk0n',
#                 consumer_secret = '9flp9kKCWMMp7DbuPGMRbFPlXxZA8f9Vr9t2YtNfWyEi8Yv4Tx',
#                 access_token_key = '1083132402862481408-33PMPC4kRYiQRUqLDhwTwrqIoQuyEk',
#                 access_token_secret = 'k5o1wWn9bswSNIOmB2R5uNWiFzBHEA5ihOeSwOvuy4R0F',
#                 tweet_mode='extended')
#
# def check_punctuation(tweet):
#     punctuation = [".","!","?"]
#     if tweet[-1] in punctuation:
#         return tweet
#     else:
#         return tweet + random.choice(punctuation)
#
#
# def get_timeline(screen_name, max_id):
#     all_updates = api.GetUserTimeline(screen_name=screen_name, count=200, exclude_replies=True, include_rts=False, max_id=max_id)
#     for status in all_updates:
#         if status == all_updates[0]:
#             pass
#         else:
#             tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', status.full_text)
#             if tweet == "":
#                 pass
#             else:
#                 tweet = re.sub(r'&amp;','&', tweet)
#                 tweet = check_punctuation(tweet)
#                 global text_archive
#                 text_archive += " " + tweet
#
#     return all_updates[-1].id
#
#
# def collect(screen_name):
#     tweet_id = get_timeline(screen_name=screen_name, max_id=None)
#     for _ in range(20):
#         tweet_id = get_timeline(screen_name=screen_name, max_id=tweet_id)
#
#     return text_archive
#
#
# # print(collect("kanyewest"))
