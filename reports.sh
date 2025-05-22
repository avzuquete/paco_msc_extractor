#!/usr/bin/sh

# set -x

bindir=`dirname $0`

nums=`ls -d [1-9]*`

new_nums=`( for i in $nums; do
    python3 $bindir/name.py < $i/personal | awk '{for (i = 2; i <= NF; i++) printf( "%s-", $i );}'
    echo
done ) | LC_ALL=pt_PT sort | sed -e "s/[^0-9]*//g"`

for i in $new_nums; do
    echo $i 1>&2
    echo "---"
    $bindir/report.sh $i
done
