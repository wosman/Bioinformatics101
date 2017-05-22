# import re
# Use the file name mbox-short.txt as the file name
#fname = raw_input("Enter file name: ")
# fname = "mbox-short.txt"
# fh = open(fname)
# number = 0
# atpos = 0
# count = 0
#
# newlist = []
# for line in fh:
#     if line.startswith("From ") :
#         listofline = line.split()
#         print listofline[1]
#         count = count +1
#
# # print listofline
# # print newlist
# print count

# name = raw_input("Enter file:")
#
# if len(name) < 1 : name = "mbox-short.txt"

# name = "real_file.txt"
# handle = open(name)

# school = dict()
#
# for line in handle :
#     if not line.startswith('From ') : continue
#     words = line.split()
#     # words = words[1].split('@')
#     addr = words[1]
#     school[addr] = school.get(addr, 0) + 1
#
# print school
#
# for occurrence in school.values():
#     # comparator = occurrence
#     # if occurence
#   print occurrence
#
# for name,occurrence in school.items():
#     if occurrence == 5:
#         print name, occurrence



# counts = dict()
#
#
# for line in handle :
#     if not line.startswith('From ') : continue
#     words = line.split()
#     words = words[5]
#     counts[words[:2]] = counts.get(words[:2], 0) + 1
#
# # print counts
#
# ltrlst = list()
#
# for k,v in counts.items():
#     ltrlst.append((k,v))
# ltrlst.sort(reverse=False)
# sortedlst = ltrlst
#
# for k,v in sortedlst:
#     print k,v


# print type(sortedlst)
#
# stackedstring =  '\n'.join(map(str, sortedlst))
#
# print stackedstring
#
# re.sub(r'[^\w]', ' ', stackedstring)
#
# print stackedstring

# numbers = []
# final_count = 0
#
# for line in handle:
    # line = line.rstrip()
    # numbers.append(re.findall('[0-9]+',line))
    # if re.findall('[0-9]+',line):
    #     for i in re.findall('[0-9]+',line):
    #         final_count = final_count + int(i)
    # if re.findall('[0-9]+',line):
    #     print line

# print numbers
#
# print final_count



# import urllib
# from BeautifulSoup import *
#
# url = 'http://python-data.dr-chuck.net/comments_42.html'
# html = urllib.urlopen(url).read()
#
# soup = BeautifulSoup(html)
#
# # print soup
# final_count = 0
# # Retrieve all of the anchor tags
# tags = soup('span')
# print tags
#
# for tag in tags:
#     # Look at the parts of a tag
#     # print 'TAG:',tag
#     # print 'URL:',tag.get('href', None)
#     print 'Contents:',tag.contents[0]
#     final_count = final_count + int(tag.contents[0])
#     # print 'Attrs:',tag.attrs
#
# print final_count

#### counts all tags
# import urllib
# from BeautifulSoup import *
#
# url = 'http://python-data.dr-chuck.net/comments_311643.html'
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)
#
# final_count = 0
#
# tags = soup('span')
# print tags
#
# for tag in tags:
#     final_count = final_count + int(tag.contents[0])
#
# print final_count


import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Rufus.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = 0
count2 = 0

position = url.find('y_')
position2 = url.find('.h')
print url[position+2:position2]

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    count = count + 1

    if count == 18:
        urllib.urlopen(tag.get('href', None)).read()
        # count = 0
        url = str(tag.get('href', None))
        position = url.find('y_')
        position2 = url.find('.h')
        print url[position + 2:position2]
        count = 0

        # print tag.get('href', None)
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        count2 = count2 + 1
        for tag in tags:
            count = count + 1

            if count == 18:
                urllib.urlopen(tag.get('href', None)).read()
                # count = 0
                url = str(tag.get('href', None))
                position = url.find('y_')
                position2 = url.find('.h')
                print url[position + 2:position2]
                count = 0

                # print tag.get('href', None)
                html = urllib.urlopen(url).read()
                soup = BeautifulSoup(html)
                tags = soup('a')
                count2 = count2 + 1
                for tag in tags:
                    count = count + 1

                    if count == 18:
                        urllib.urlopen(tag.get('href', None)).read()
                        # count = 0
                        url = str(tag.get('href', None))
                        position = url.find('y_')
                        position2 = url.find('.h')
                        print url[position + 2:position2]
                        count = 0

                        # print tag.get('href', None)
                        html = urllib.urlopen(url).read()
                        soup = BeautifulSoup(html)
                        tags = soup('a')
                        count2 = count2 + 1
                        for tag in tags:
                            count = count + 1

                            if count == 18:
                                urllib.urlopen(tag.get('href', None)).read()
                                # count = 0
                                url = str(tag.get('href', None))
                                position = url.find('y_')
                                position2 = url.find('.h')
                                print url[position + 2:position2]
                                count = 0

                                # print tag.get('href', None)
                                html = urllib.urlopen(url).read()
                                soup = BeautifulSoup(html)
                                tags = soup('a')
                                count2 = count2 + 1
                                for tag in tags:
                                    count = count + 1

                                    if count == 18:
                                        urllib.urlopen(tag.get('href', None)).read()
                                        # count = 0
                                        url = str(tag.get('href', None))
                                        position = url.find('y_')
                                        position2 = url.find('.h')
                                        print url[position + 2:position2]
                                        count = 0

                                        # print tag.get('href', None)
                                        html = urllib.urlopen(url).read()
                                        soup = BeautifulSoup(html)
                                        tags = soup('a')
                                        count2 = count2 + 1
                                        for tag in tags:
                                            count = count + 1

                                            if count == 18:
                                                urllib.urlopen(tag.get('href', None)).read()
                                                # count = 0
                                                url = str(tag.get('href', None))
                                                position = url.find('y_')
                                                position2 = url.find('.h')
                                                print url[position + 2:position2]
                                                count = 0

                                                # print tag.get('href', None)
                                                html = urllib.urlopen(url).read()
                                                soup = BeautifulSoup(html)
                                                tags = soup('a')
                                                count2 = count2 + 1
                                                for tag in tags:
                                                    count = count + 1
                        
                                                    if count == 18:
                                                        urllib.urlopen(tag.get('href', None)).read()
                                                        # count = 0
                                                        url = str(tag.get('href', None))
                                                        position = url.find('y_')
                                                        position2 = url.find('.h')
                                                        print url[position + 2:position2]
                                                        break
