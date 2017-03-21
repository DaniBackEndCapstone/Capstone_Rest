import csv
import sqlite3

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

with sqlite3.connect("../../db.sqlite3") as db:
    cursor = db.cursor()

    for row in iter_data:
        state_or_territory = row[1]
        total_female_supervised = int(row[4].replace(",", ""))
        total_female_incarcerated = int(row[9].replace(",", ""))
        total_male_supervised =  int(row[3].replace(",", ""))
        total_male_incarcerated = int(row[8].replace(",", ""))

        print(state_or_territory, total_female_supervised, total_female_incarcerated, total_male_supervised, total_male_incarcerated)

        cursor.execute("""
            UPDATE capstone_api_statedata
            SET total_female_supervised={}, total_female_incarcerated={}, total_male_supervised={}, total_male_incarcerated={}
            WHERE state_or_territory='{}'
                """.format(total_female_supervised, total_female_incarcerated, total_male_supervised, total_male_incarcerated, state_or_territory))



