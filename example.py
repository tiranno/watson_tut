#!/usr/bin/env python

import sys
import urllib
import urllib2
import json

if len(sys.argv) != 2:
  print('Usage: ./watson_prog <sentence in your language of choice>')

# curl -u "9fdda5be-7c24-4565-a13b-341d5098d806":"IaevO0SytB0m"  "https://gateway.watsonplatform.net/language-translation/api/v2/identifiable_languages"
URL = "https://gateway.watsonplatform.net/language-translation/api/v2/identify"
USER = "9fdda5be-7c24-4565-a13b-341d5098d806"
PASS = "IaevO0SytB0m"
USERPASSWORD = USER + ":" + PASS
encoding = USERPASSWORD.encode('utf-8')

example_sentence = sys.argv[1]
POSTSTRING = "d="+example_sentence
POST = POSTSTRING.encode('utf-8')
postdatabytes = bytes(POST)

# Send POST to Bluemix language id service
req = urllib2.Request()
values = {} 
settings = urllib.urlencode()

# Get response from server (ie: the language code itself)
language_code = 'LANG_NOT_FOUND'


# Parse through JSON list of all language codes to find corresponding wikipedia article
full_string = '{"en":"https://en.wikipedia.org/wiki/English_language", "es":"https://en.wikipedia.org/wiki/Spanish_language","LANG_NOT_FOUND":"Language was unable to be identified by the service."}'
parsed_json = json.loads(full_string)

# Print the URL to the terminal.
print (parsed_json[language_code])













