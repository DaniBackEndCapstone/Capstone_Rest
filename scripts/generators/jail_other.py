import csv
# import sqlite3


def get_jail_other_data_parse_into_lists(NumberOfPersonsIncarceratedByOtherAdultCorrectionalFacilites2015):
    """
    Method that will read from the CSV file titled NumberOfPersonsIncarceratedByOtherAdultCorrectionalFacilites2015
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(NumberOfPersonsIncarceratedByOtherAdultCorrectionalFacilites2015, "r", encoding="latin-1") as jail_other_data:
        for jail_other_data in csv.reader(jail_other_data):
            yield jail_other_data

if __name__ == '__main__':
    filename = "../excel_files/NumberOfPersonsIncarceratedByOtherAdultCorrectionalFacilites2015.csv"
    iter_data = iter(get_jail_other_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        print(iter_data)
        total_other_prison = row[5]
        print(total_other_prison)

