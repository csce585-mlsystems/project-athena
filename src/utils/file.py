"""
Implement file i/o operations.
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import csv
from enum import Enum
import json


def read_list_from_file(file):
    """
    Read a text file into a list, with each line as an element.
    """
    with open(file) as f:
        contents = f.read().splitlines()
    return contents


def load_from_json(file):
    """
    Load contents from a json file into a dictionary
    :param file:
    :return:
    """
    with open(file, 'r') as json_file:
        dict = json.load(json_file)

    return dict


def dump_to_json(dict, file):
    """
    Dump a dictionary to a json file.
    :param dict:
    :param file:
    :return:
    """
    with open(file, 'w') as json_file:
        json.dump(dict, json_file)

    return True


class CSV_ORIENT(Enum):
    COL = "col"
    ROW = "row"


def dict2csv(dictionary, file_name, list_as_value=False, append=False):
    """
    Serialize values in given dictionary to a csv file.
    :param dictionary: the dictionary to save.
    :param file_name: the name of the csv file, including the path.
    :param list_as_value: each key has a list of values.
    """
    print(dictionary)

    if append:
        with open(file_name, 'a+', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            if list_as_value:
                writer.writerow(dictionary.keys())
                writer.writerows(zip(*dictionary.available_values()))
            else:
                for row in dictionary.items():
                    writer.writerow(row)
    else:
        with open(file_name, 'w') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            if list_as_value:
                """
                The dictionary is in form of
                {
                key : [values]
                }
                """
                writer.writerow(dictionary.keys())
                writer.writerows(zip(*dictionary.available_values()))
            else:
                """
                The dictionary is in form of
                {
                key : value
                }
                """
                for row in dictionary.items():
                    writer.writerow(row)


def csv2dict(file_name, orient=CSV_ORIENT.COL.value, dtype='float'):
    """
    Load csv into a dictionary in the form of
    {
        key : [values]
    }
    :param file_name: csv file name includes the full path
    :param orient:
        orient.col: values of the keys are in a column
        orient.row: values of the keys are in a row
    :param dtype: data type of values
    :return: the dictionary
    """
    if CSV_ORIENT.COL.value == orient:
        with open(file_name) as file:
            reader = csv.reader(file)
            col_headers = next(reader, None)

            columns = {}
            for header in col_headers:
                columns[header] = []

            for row in reader:
                for header, value in zip(col_headers, row):
                    if 'float' == dtype:
                        value = float(value)
                    columns[header].append(value)

        return columns

    else: # CSV_ORIENT.COL.value == orient
        raise NotImplemented
        # rows = {}
        # return rows
