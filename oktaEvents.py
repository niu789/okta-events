from datetime import datetime, tzinfo, timedelta
import json
import re
import requests
import sys

org = sys.argv[1]
token = sys.argv[2]
startTime = sys.argv[3]

#url = 'https://' + org + '.okta.com/api/v1/events'
url = 'https://' + org + '.okta.com/api/v1/logs'
headers = { 'Authorization': 'SSWS ' + token }
#now = datetime.now()

# Okta API breaks with microseconds
#params = { 'startDate': startTime.isoformat()[:-3] + 'Z' }
#params = { 'startDate': startTime[:-3] + 'Z' }
params = { 'since': startTime[:-3] + 'Z' }

events = requests.get(url, headers=headers, params=params)
#events.text
i = 0
for e in events.json():
    if i == 0:
        i += 1
        continue
    print (json.dumps(e))

#while 'next' in events.links:
#    events = requests.get(events.links['next']['url'], headers=headers)
#    for e in events.json():
#        print (e)
