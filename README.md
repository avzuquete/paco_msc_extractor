# paco_msc_extractor
Tools to extract students applications into a single MD or HTML file

## Instructions

1. Go to the applications' page and log in.
2. Extract the session cookie to a file (check the cookie file example). You can use the browser inspector, trace network accesses, access one page of the applications, select one HTTP access to paco.ua.pt, then get the cookie line from the raw headers.
3. Get the Excel file will all the applicants, copy their number and store in one file, one number per line.
4. Use the headers file provided.
5. Run the command `extract.sh cookie_file headers_file numbers_file`. This creates one directory per student number, with one file per information page in Paco.
6. Run the command "`reports.sh to create a Markdown file with the information of all the stdents, ordered by their name (as in Paco). Output to Stdout.
7. Run the comamnd "`md2html` to create an HTML file from the Markdown one. Use Stdin and Stdout.

## Aditional information

The final report contains links to sipplementary information in Paco, when releant. Those links open a new tab.

There are some Python3 scripts, which require the modules BeautifulSoup and markdown
