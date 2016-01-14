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
    return urllib2.urlopen(url).read()

if len(sys.argv) != 2:
  print('Usage: ./watson_tut <hello in your language of choice>')
  sys.exit()

url = "https://gateway.watsonplatform.net/language-translation/api/v2/identifiable_languages"
ident_lang = json.loads(f_call_watson(url, ""))

url = "https://gateway.watsonplatform.net/language-translation/api/v2/identify?text=" + sys.argv[1]
lang_code = f_call_watson(url, "")

print(ident_lang)
print(lang_code)
