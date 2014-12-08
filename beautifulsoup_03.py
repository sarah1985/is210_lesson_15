#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Lesson 15"""

import urllib2
from bs4 import BeautifulSoup

URL = 'http://sps.cuny.edu/whoweare/departments/it'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)


def sps_it_department():
    """sps it contacts"""

    soup_names = SOUP.html.find_all("span", {"class": "name bold"})
    emails = SOUP.select("a[href^=mailto]")

    contacts = []
    for index in range(len(soup_names)):
        full_name = soup_names[index].get_text().split(',')
        first_name = full_name[1].strip()
        last_name = full_name[0].strip()
        email = emails[index].get_text()

        contact_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }

        contacts.append(contact_dict)

    return contacts

if __name__ == '__main__':
    print sps_it_department()