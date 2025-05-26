#!/usr/bin/python3

import markdown
import sys

html_content = markdown.markdown( sys.stdin.read() )

sys.stdout.write( '<html>\n<meta charset="UTF-8">\n' )
sys.stdout.write( html_content.replace( '<a href=', '<a target="_blank" href=' ) )
sys.stdout.write( '\n</html>\n' )
