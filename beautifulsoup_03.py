import urllib2
from bs4 import BeautifulSoup

URL = 'http://sps.cuny.edu/whoweare/departments/it'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)

# Put your function here

if __name__ == '__main__':
    # You can use this conditional block for debugging
    # print SOUP
    pass