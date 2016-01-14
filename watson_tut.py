#!/usr/bin/env python

import sys
import urllib
import urllib2
import json
import wikipedia
import webbrowser

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
  print("Usage: ./watson_tut <hello in your language of choice>")
  sys.exit()

url = "https://gateway.watsonplatform.net/language-translation/api/v2/identifiable_languages"
ident_lang = json.loads(f_call_watson(url, ""))

url = "https://gateway.watsonplatform.net/language-translation/api/v2/identify?text=" + sys.argv[1]
lang_code = f_call_watson(url, "")

language = ''
for ent in ident_lang[u'languages']:
    if ent[u'language'] == lang_code:
        language = ent[u'name']

print(lang_code)
print(language)
webbrowser.open("https://en.wikipedia.org/wiki/" + language + "_language")

wikipedia.set_lang(lang_code)
print(wikipedia.summary(language + "_language"))
