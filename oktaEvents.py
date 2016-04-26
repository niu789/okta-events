from datetime import datetime, tzinfo, timedelta
import json
import re
import requests
import sys

org = sys.argv[1]
token = sys.argv[2]
relative_cutoff_secs = sys.argv[3]

url = 'https://' + org + '.okta.com/api/v1/events'
headers = { 'Authorization': 'SSWS ' + token }
now = datetime.now()
startTime = now - timedelta(0,int(relative_cutoff_secs))
# Okta API breaks with microseconds
params = { 'startDate': startTime.isoformat()[:-3] + 'Z' }

events = requests.get(url, headers=headers, params=params)
for e in events.json():
    print e

while 'next' in events.links:
    events = requests.get(events.links['next']['url'], headers=headers)
    for e in events.json():
        print e
