__author__ = 'yotam'

from pprint import pprint
import json
import csv


json_data_persons = open('../persons_and_polyorg/data_fixture_persons.json', mode='wb')

person_csv = csv.DictReader(open('../persons_and_polyorg/data_from_json_persons.person.csv', 'r'))
person_atlname_csv = csv.DictReader(open('../persons_and_polyorg/data_from_json_persons.personaltname.csv', 'r'))
title_csv = csv.DictReader(open('../persons_and_polyorg/data_from_json_persons.title.csv', 'r'))


def turn_csv_to_dict(dict_reader_object):
    list_of_dicts_for_insertion = []
    for row in dict_reader_object:
        full_dict = dict()
        full_dict['pk'] = row.pop('pk')
        full_dict['model'] = row.pop('model')
        fields_dict = dict()
        for key, value in row.items():
            if key in ['content_type', 'titles'] or value == "None":
                fields_dict[key] = eval(value)
            elif value == "TRUE":
                fields_dict[key] = True
            elif value == "FALSE":
                fields_dict[key] = False
            else:
                fields_dict[key] = value
        full_dict['fields'] = fields_dict
        list_of_dicts_for_insertion.append(full_dict)

    pprint(list_of_dicts_for_insertion)
    return list_of_dicts_for_insertion


def main():
    all_persons_data_for_insertion = turn_csv_to_dict(person_csv) + \
                                     turn_csv_to_dict(title_csv) + \
                                     turn_csv_to_dict(person_atlname_csv)

    print 'creating persons data fixture'
    pprint(all_persons_data_for_insertion)
    json.dump(all_persons_data_for_insertion, json_data_persons, encoding='utf-8', indent=4)
    json_data_persons.close()


if __name__ == "__main__":
    main()


