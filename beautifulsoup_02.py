#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Lesson 15"""

import urllib2
from bs4 import BeautifulSoup

URL = 'http://www.whitehouse.gov/net-neutrality'
DATA = urllib2.urlopen(URL).read()
HTML_SOUP = BeautifulSoup(DATA)


def obama_net_neutrality():
    """obama net neutrality beautifulsoup"""

    statement = HTML_SOUP.find("p", {"class": "displayed"})

    return statement


if __name__ == '__main__':
    print HTML_SOUP
    print obama_net_neutrality()