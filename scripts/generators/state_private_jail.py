import csv


def get_state_private_jail_data_parse_into_lists(PrisonersUnderJurisdictionOfStateAndPrivatePrisons20142015):
    """
    Method that will read from the CSV file titled PrisonersUnderJurisdictionOfStateAndPrivatePrisons20142015
    and parse CSV data into lists by line. The model will then post the data into the StateData model using the create object.
    Author: Dani Adkins
    """
    with open(PrisonersUnderJurisdictionOfStateAndPrivatePrisons20142015, "r", encoding="latin-1") as state_private_jail_data:
        for state_private_jail_data in csv.reader(state_private_jail_data):
            yield state_private_jail_data

if __name__ == '__main__':
    filename = "../excel_files/PrisonersUnderJurisdictionOfStateAndPrivatePrisons20142015.csv"
    iter_data = iter(get_state_private_jail_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        state = row[1]
        total_private = row[3]
        total_local_jail = row[9]
        # print(state, total_private_2015)
        # print(state, total_local_jail_2015)

        StateData.objects.create(
            state = row[1],
            total_private = row[3],
            total_local_jail = row[9]
        )

