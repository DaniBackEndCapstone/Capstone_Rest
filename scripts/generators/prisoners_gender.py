import csv


def get_gender_data_parse_into_lists(NumberPersonsCorrectionalFacilityBySexAndStatus):
    """
    Method that will read from the CSV file titled NumberPersonsCorrectionalFacilityBySexAndStatus
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(NumberPersonsCorrectionalFacilityBySexAndStatus, "r", encoding="latin-1") as gender_data:
        for gender_data in csv.reader(gender_data):
            yield gender_data

if __name__ == '__main__':
    filename = "../excel_files/NumberPersonsCorrectionalFacilityBySexAndStatus.csv"
    iter_data = iter(get_gender_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        state = row[1]
        total_female_supervised = row[4]
        total_female_incarcerated = row[9]
        total_male_supervised =  row[3]
        total_male_incarcerated = row[8]

        # print(state, total_female_supervised)
        # print(state, total_female_incarcerated)
        # print(state, total_male_supervised)
        # print(state, total_male_incarcerated)

        StateData.objects.create(
            state = row[1],
            total_female_supervised = row[4],
            total_female_incarcerated = row[9],
            total_male_supervised =  row[3],
            total_male_incarcerated = row[8]
        )

