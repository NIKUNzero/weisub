import json
import config
import random
import time
from requests_oauthlib import OAuth1Session

def tweet(content):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    AS = config.ACCESS_TOKEN_SECRET

    twitter = OAuth1Session(CK, CS, AT, AS)
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status" : content}

    req = twitter.post(url, params = params)

def main():
    str = 'さふうぇい"'
    char_list = list(str)
    output = random.sample(char_list, 6)
    sta = ""
    for i in output:
        sta += i
    return sta
