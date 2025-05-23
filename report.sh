#!/usr/bin/sh

# set -x

if [ "$#" != "1" ]; then
    echo "usage: $0 student_number" 1>&2
    exit 1
fi

number=$1
bindir=`dirname $0`

python3 $bindir/name.py < $number/personal
echo
python3 $bindir/education.py < $number/education
echo
python3 $bindir/conferences.py < $number/conferences
echo
python3 $bindir/publications.py < $number/publications
echo
python3 $bindir/experience.py < $number/experience
echo
python3 $bindir/languages.py < $number/languages
echo
python3 $bindir/volunteering.py < $number/volunteering
echo
python3 $bindir/attachments.py < $number/attachment
