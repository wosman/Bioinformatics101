import urllib
import xml.etree.ElementTree as ET


while True:
    address = raw_input('Enter location: ')
    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    # print data
    tree = ET.fromstring(data)
    results = tree.findall('.//count')
    index = 0
    print 'Count:' + str(len(results))
    for item in results:
        index = index + int(item.text)
    print index
