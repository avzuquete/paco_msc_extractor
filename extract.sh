#!/bin/sh

# set -x

if [ "$#" != "3" ]; then
    echo "usage: $0 cookie_file headers_file numbers_file" 1>&2
    exit 1
fi

cookie=$1
headers=$2
numbers=$3

decompress()
{
    zcat < data.zip > $1
    rm data.zip
}

for number in `cat $numbers`; do
    mkdir $number
    cd $number

    cp ../$headers .
    cat ../$cookie >> headers
    echo "Referer: https://paco.ua.pt/Candidaturas/BackOffice/ContestApplication/Summary/$number" >> headers

    curl -L -H @headers https://paco.ua.pt/Candidaturas/PersonalInfo/Details/$number -o data.zip
    decompress personal
    curl -L -H @headers https://paco.ua.pt/Candidaturas/HigherEducation/$number -o data.zip
    decompress education
    curl -L -H @headers https://paco.ua.pt/Candidaturas/ProfessionalEducation/$number -o data.zip
    decompress conferences
    curl -L -H @headers https://paco.ua.pt/Candidaturas/Publication/$number -o data.zip
    decompress publications
    curl -L -H @headers https://paco.ua.pt/Candidaturas/ProfessionalExperience/$number -o data.zip
    decompress experience
    curl -L -H @headers https://paco.ua.pt/Candidaturas/LanguageKnowledge/$number -o data.zip
    decompress languages
    curl -L -H @headers https://paco.ua.pt/Candidaturas/Volunteering/$number -o data.zip
    decompress volunteering
    curl -L -H @headers https://paco.ua.pt/Candidaturas/Attachment/$number -o data.zip
    decompress attachment
    cd ..
done
