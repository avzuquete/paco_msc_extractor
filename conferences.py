#!/usr/byn/python3

from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup( sys.stdin, 'html.parser' )

for table in soup.find_all( class_='table' ):
    th = table.find_all( 'th' )
    if th[1].text.strip()[0:2] == 'Ac':
        print( '## Formação profisional\n' )

        for tr in table.find_all( 'tr' ):
            td = tr.find_all( 'td' )
            if len( td ) == 0:
                continue
            link = 'https://paco.ua.pt/' + tr.find( 'a', href=True )['href']
            print( "- **[%s](%s)**: %s (data = %s)" % (td[1].text.strip(), link, td[2].text.strip(), td[3].text.strip()) )

    elif th[1].text.strip()[0:2] == 'Ti':
        print( '\n## Conferências\n' )

        for tr in table.find_all( 'tr' ):
            td = tr.find_all( 'td' )
            if len( td ) == 0:
                continue
            print( "- **%s**: %s, %s (%s)" % (td[1].text.strip(), td[2].text.strip(), td[3].text.strip(), td[4].text.strip()) )
