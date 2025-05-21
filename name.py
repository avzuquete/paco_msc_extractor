#!/usr/byn/python3

from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup( sys.stdin, 'html.parser' )

div = soup.find( class_='contest_application_header' )
div = div.find( class_='row' )
div = div.find( class_='col-md-9' )
h = div.find( 'h4' )
name = div.find( 'small' )
names = name.text.strip()[2:].split()

name = ''

for i in range(len(names) - 1):
    name += names[i][0] + names[i][1:].lower() + ' '

name += names[-1]

print( '# %s' % name )
