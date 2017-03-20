import csv


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
        # type_of_jail = row[0]
        total_other_prison = row[5]
        # print(type_of_jail, total_in_other_2015)



        # cursor.execute("""
        #         UPDATE capstone_api_statedata

        #         VALUES total_other_prison
        #         WHERE State=state

        #         state, total_private, total_local_jail)VALUES
        #         (null, '{}', {}, {}
        #         )""".format(state, total_private, total_local_jail))