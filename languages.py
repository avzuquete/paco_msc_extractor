#!/usr/byn/python3

from bs4 import BeautifulSoup
import sys

print( '## Conhecimento de Línguas\n' )

soup = BeautifulSoup( sys.stdin, 'html.parser' )

table = soup.find( class_='table' )

if table == None:
    sys.exit( 0 ) 

for tr in table.find_all( 'tr' ):
    # print( tr )
    td = tr.find_all( 'td' )
    if len( td ) == 0:
        continue

    print( "- **%s**:\n    * **compreensão oral**: %s\n    * **leitura**: %s\n    * **interação oral**: %s\n    * **produção oral**: %s\n    * **escrita**: %s" % (td[1].text.strip(), td[2].text.strip(), td[3].text.strip(), td[4].text.strip(), td[5].text.strip(), td[6].text.strip()) )
