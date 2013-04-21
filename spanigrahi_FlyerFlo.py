# spanigrahi_FlyerFlo.py
# Finds and downloads the subreddit header image given the URL.
import urllib2
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup # for HTML parsing

url = "http://flyerflo.us4.list-manage.com/track/click?u=3cfaa07738f14f5822fcc51fb&id=4d7da39746&e=0f305dcf8b"
urlContent = urllib2.urlopen(url).read()
soup = BeautifulSoup(''.join(urlContent))
imgTags = soup.findAll('img') # find all image tags

# download all images
for imgTag in imgTags:
    imgCheck = imgTag['id']
    if imgCheck == 'header-img': # finds the header image based on the id tag
        imgUrl = imgTag['src']
        try:
            imgData = urllib2.urlopen(imgUrl).read()
            fileName = basename(urlsplit(imgUrl)[2])
            output = open(fileName,'wb')
            output.write(imgData)
            output.close()
        except:
            pass
