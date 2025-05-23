
#!/usr/byn/python3

from bs4 import BeautifulSoup
import sys

print( '## Anexos\n' )

soup = BeautifulSoup( sys.stdin, 'html.parser' )

table = soup.find( class_='table' )

if table == None:
    sys.exit( 0 )

for tr in table.find_all( 'tr' ):
    td = tr.find_all( 'td' )
    if len( td ) == 0:
        continue

    link = 'https://paco.ua.pt/' + tr.find( 'a', href=True )['href']

    # print( td[2].text.strip() )

    if td[1].text.strip()[0:8] == 'Habilita':
        print( "- [**Habilitação**](%s)" % (link) )
    elif td[2].text.strip()[-9:-4] == 'stica':
        print( "- [**Inglês**](%s)" % (link) )
    elif td[1].text.strip()[:5] == 'Outra':
        print( "- [**Outra**](%s)" % (link) )
