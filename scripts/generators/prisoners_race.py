import csv
import sqlite3

def get_prisoners_by_race_data_parse_into_lists(PrisonersUnderJurisdicitonOfStateOrFederalByRace2015):
    """
    Method that will read from the CSV file titled PrisonersUnderJurisdicitonOfStateOrFederalByRace2015
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(PrisonersUnderJurisdicitonOfStateOrFederalByRace2015, "r", encoding="latin-1") as prisoners_race_data:
        for prisoners_race_data in csv.reader(prisoners_race_data):
            yield prisoners_race_data

if __name__ == '__main__':
    filename = "../excel_files/PrisonersUnderJurisdicitonOfStateOrFederalByRace2015.csv"
    iter_data = iter(get_prisoners_by_race_data_parse_into_lists(filename))
    next(iter_data)

with sqlite3.connect("../../db.sqlite3") as db:
    cursor = db.cursor()

    for row in iter_data:
        state_or_territory = row[0]
        race_white = int(row[2].replace(",", "").replace("/", "0").replace("~", "0"))
        race_black = int(row[3].replace(",", "").replace("/", "0").replace("~", "0"))
        race_hispanic = int(row[4].replace(",", "").replace("/", "0").replace("~", "0"))
        race_american_indian_alaska_native = int(row[5].replace(",", "").replace("/", "0").replace("~", "0"))
        race_asian = int(row[6].replace(",", "").replace("/", "0").replace("~", "0"))
        race_native_hawaiian_pacific_islander = int(row[7].replace(",", "").replace("/", "0").replace("~", "0"))
        race_two_or_more = int(row[8].replace(",", "").replace("/", "0").replace("~", "0"))
        race_other = row[9].replace(",", "").replace("/", "0").replace("~", "0")
        race_unknown = int(row[10].replace(",", "").replace("/", "0").replace("~", "0"))

        print(state_or_territory, race_white, race_black, race_hispanic, race_american_indian_alaska_native, race_asian, race_native_hawaiian_pacific_islander, race_two_or_more, race_other, race_unknown)

        cursor.execute("""
            UPDATE capstone_api_statedata
            SET race_white={}, race_black={}, race_hispanic={}, race_american_indian_alaska_native={}, race_asian={}, race_native_hawaiian_pacific_islander={}, race_two_or_more={}, race_other={}, race_unknown={}
            WHERE state_or_territory='{}'
                """.format(race_white, race_black, race_hispanic, race_american_indian_alaska_native, race_asian, race_native_hawaiian_pacific_islander, race_two_or_more, race_other, race_unknown, state_or_territory))





