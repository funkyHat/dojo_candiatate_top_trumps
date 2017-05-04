#! /usr/bin/env python3

import csv

data = {}


def rank_birth_date(date):
    return int(date.replace('-', ''))


fields = {
    'name': None,
    'party_name': None,
    'honorific_prefix': None,
    'birth_date': rank_birth_date,
    'twitter_username': None,
    'homepage_url': None,
    }


with open('candidates-all.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        person = data.setdefault(row['name'], {})
        for field, func in fields.items():
            if row[field] and func:
                score = func(row[field])
                person[field] = max(person.get(field, 0), score)
