#!/usr/byn/python3

from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup( sys.stdin, 'html.parser' )

# There is only one table with the courses

table = soup.find_all( class_='table' )

# print( entry )

print( '## Habilitações académicas\n' )

for tr in table[0].find_all( 'tr' ):
    # print( tr )
    td = tr.find_all( 'td' )
    if len( td ) == 0:
        continue

    link = 'https://paco.ua.pt/' + tr.find( 'a', href=True )['href']
    print( "- **%s**: %s, [%s](%s) (nota = %s, data = %s)" % (td[1].text.strip(), td[2].text.strip(), td[3].text.strip(), link, td[4].text.strip(), td[5].text.strip()) )

if len(table) == 2:
    print( '\n### Habilitações preferenciais\n' )

    for tr in table[1].find_all( 'tr' ):
        # print( tr )
        td = tr.find_all( 'td' )
        if len( td ) == 0:
            continue

        if td[3].text.strip()[0] == 'N':
            print( "- **%s**: %s, %s (não concluído, ECTS = %s, média atual = %s, inscrito = %s)" % (td[0].text.strip(), td[1].text.strip(), td[2].text.strip(), td[4].text.strip(), td[5].text.strip(), td[6].text.strip()) )
        else:
            print( "- **%s**: %s, %s (concluído, nota = %s, data = %s)" % (td[0].text.strip(), td[1].text.strip(), td[2].text.strip(), td[4].text.strip(), td[5].text.strip()) )
