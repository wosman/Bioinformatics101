import json
import urllib

address = raw_input('Enter location: ')
url = address
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
info = json.loads(data)
comments = info['comments']
print 'Count: ' + str(len(comments))
index=0
for item in comments:
    index = index + int(item['count'])
print 'Sum: ' + str(index)