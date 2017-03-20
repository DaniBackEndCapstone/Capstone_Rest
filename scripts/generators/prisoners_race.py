import csv

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

    for row in iter_data:
        state = row[0]
        race_white = row[2]
        race_black = row[3]
        race_hispanic = row[4]
        race_american_indian_alaska_native = row[5]
        race_asian = row[6]
        race_native_hawaiian_pacific_islander = row[7]
        race_two_or_more = row[8]
        race_other = row[9]
        race_unknown = row[10]

        # print(state, race_white)
        # print(state, race_black)
        # print(state, race_hispanic)
        # print(state, race_american_indian_alaska_native)
        # print(state, race_asian)
        # print(state, race_native_hawaiian_pacific_islander)
        # print(state, race_two_or_more)
        # print(state, race_other)
        # print(state, race_unknown)


        StateData.objects.create(
            state=row[0],
            race_white=row[2],
            race_black=row[3],
            race_hispanic=row[4],
            race_american_indian_alaska_native=row[5],
            race_asian=row[6],
            race_native_hawaiian_pacific_islander=row[7],
            race_two_or_more=row[8],
            race_other=row[9],
            race_unknown=row[10],
        )

