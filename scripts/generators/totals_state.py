import csv

def get_correctional_totals_data_parse_into_lists(EstimatedNumberAndRateOfPersonsSupervisedByUSFacilities2015):
    """
    Method that will read from the CSV file titled EstimatedNumberAndRateOfPersonsSupervisedByUSFacilities2015
    and parse CSV data into lists by line. The for statement will then iterate over the data and set each row equal to the information contained in that row.
    Author: Dani Adkins
    """
    with open(EstimatedNumberAndRateOfPersonsSupervisedByUSFacilities2015, "r", encoding="latin-1") as correctional_totals_data:
        for correctional_totals_data in csv.reader(correctional_totals_data):
            yield correctional_totals_data

if __name__ == '__main__':
    filename = "../excel_files/EstimatedNumberAndRateOfPersonsSupervisedByUSFacilities2015.csv"
    iter_data = iter(get_correctional_totals_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        state = row[1]
        total_correction_pop = row[2]
        total_correction_pop_per_one_hundred_thou_residents_all = row[4]
        total_pop_incarcerated = row[8]
        total_pop_incarcerated_per_one_hundred_thou_residents_all = row[10]
        # print(state, total_correction_pop)
        # print(state, total_correction_pop_per_one_hundred_thou_residents_all)
        # print(state, total_pop_incarcerated)
        # print(state, total_pop_incarcerated_per_one_hundred_thou_residents_all)

        StateData.objects.create(
            state=row[1],
            total_correction_pop=row[2],
            total_pop_incarcerated=row[8],
            total_correction_pop_per_one_hundred_thou_residents_all=row[4],
            total_pop_incarcerated_per_one_hundred_thou_residents_all=row[10]
        )
