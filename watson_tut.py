#!/usr/bin/env python

import sys
import urllib2

if len(sys.argv) != 2:
  print('Usage: ./watson_prog <hello in your language of choice>')

# curl -u "9fdda5be-7c24-4565-a13b-341d5098d806":"IaevO0SytB0m"  "https://gateway.watsonplatform.net/language-translation/api/v2/identifiable_languages"
URL = "https://gateway.watsonplatform.net/language-translation/api/v2/identifiable_languages"
USER = "9fdda5be-7c24-4565-a13b-341d5098d806"
PASS = "IaevO0SytB0m"

print ()
