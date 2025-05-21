
#!/usr/byn/python3

from bs4 import BeautifulSoup
import sys

print( '## Voluntariado\n' )

soup = BeautifulSoup( sys.stdin, 'html.parser' )

table = soup.find( class_='table' )

if table == None:
    sys.exit( 0 )

for tr in table.find_all( 'tr' ):
    td = tr.find_all( 'td' )
    if len( td ) == 0:
        continue

    link = 'https://paco.ua.pt/' + tr.find( 'a', href=True )['href']
    print( "- [**%s**](%s) (%s a %s)" % (td[1].text.strip(), link, td[2].text.strip(), td[3].text.strip()) )
