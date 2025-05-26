# paco_msc_extractor
Tools to extract students applications into a single MD or HTML file

## Instructions

1. Go to the applications' page and log in.
2. Get the Excel file will all the applicants, copy their number and store in a plain text file, one number per line. You may want to remove students that haven't payed from the list of numbers.
3. Extract the session cookie to a file (check the example in the cookie file). You can use the browser inspector, trace network accesses, access one page of the applications, select one HTTP access to paco.ua.pt, then get the cookie line from the raw headers.
4. Run the command `extract.sh cookie_file headers numbers_file`. (note: use the headers file provided).
This creates one directory per student number, with one file per information page in Paco.
5. Run the command reports.sh to create a Markdown file with the information of all the stdents, ordered by their name (as in Paco). Redirect output to a file, for example `reports.sh > out.md`.
6. Run the comamnd md2html to create an HTML file from the Markdown one. Redirect input output, for example,`md2html < out.md > out.html`.

## Requirements

There are some Python3 scripts, which require the modules BeautifulSoup and markdown.

Python modules can be installed in different ways, both using generic OS packages (e.g. in Linux) or using Python's modules installed via pip.
When using Python's modules you can also use a virtual environment to avoid adding more packages to your OS or to your account directory.

In Linux the relevant packages are **python3-bs4** or **python3-beautifulsoup4** (for BeautifulSoup) and **python3-markdown**.
Python's modules are **beautifullsoup4** and **markdown**.

For installing the required modules with pip use the provided requirements.txt file and run `pip install -r requirements.txt` 

## Aditional information

The final report contains links to supplementary information in Paco, when releant. Those links open a new tab.

