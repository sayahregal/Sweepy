_author_ = 'Sayahnubeneklis'
#!/usr/bin/env python
# -*- coding: utf-8 -*

import tweepy, time, sys

CONSUMER_KEY = 'AVoBhZgPaSxKT8Vk1fMeJHRX0'
CONSUMER_SECRET = 'GCrCWjlZz26m1cURSvSCoAaNNLixDW7zaKIdXtjrhDjtp5d84M'
ACCESS_KEY = '3161120551-lctmTUpAcYYcUari5Y9Vl54CT8HyLcaut8efXjY'
ACCESS_SECRET = 'htmwjCHLxAvZPtOObk1ANftDhqhdkpj6AjqZbh603P85b'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('Swensong1.txt','Swen1.JPG,' 'r')
f=filename.readlines()
filename.close()

for line in f: 
  api.update_status(status=line)
  print line
  time.sleep(900)