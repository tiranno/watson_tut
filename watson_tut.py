#!/usr/bin/env python

import sys
import urllib
import urllib2
import json


def f_call_watson (url, query):
    USER = "9fdda5be-7c24-4565-a13b-341d5098d806"
    PASS = "IaevO0SytB0m"

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, USER, PASS)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)


if len(sys.argv) != 2:
  print('Usage: ./watson_prog <hello in your language of choice>')

# curl -u "9fdda5be-7c24-4565-a13b-341d5098d806":"IaevO0SytB0m"  "https://gateway.watsonplatform.net/language-translation/api/v2/identifiable_languages"
# url = "https://gateway.watsonplatform.net/language-translation/api/v2/identifiable_languages"
# f_call_watson(url, "")

url = "https://gateway.watsonplatform.net/language-translation/api/v2/identify?text=come"
f_call_watson(url, "")


response = urllib2.urlopen(url).read()

print(json.loads(response))
