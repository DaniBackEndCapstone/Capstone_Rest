import csv
import sqlite3

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

    with sqlite3.connect("../../db.sqlite3") as db:
        cursor = db.cursor()

        for row in iter_data:
            state_or_territory = row[1]
            total_correction_pop = int(row[2].replace(",", "").replace("/", "0"))
            total_correction_pop_per_one_hundred_thou_residents_all = int(row[4].replace(",", "").replace("/", "0"))
            total_pop_incarcerated = int(row[8].replace(",", "").replace("/", "0"))
            total_pop_incarcerated_per_one_hundred_thou_residents_all = int(row[10].replace(",", "").replace("/", "0"))

            print(state_or_territory, total_correction_pop, total_correction_pop_per_one_hundred_thou_residents_all, total_pop_incarcerated, total_pop_incarcerated_per_one_hundred_thou_residents_all)

            cursor.execute("""
                INSERT INTO capstone_api_statedata(id, state_or_territory, total_correction_pop, total_correction_pop_per_one_hundred_thou_residents_all, total_pop_incarcerated, total_pop_incarcerated_per_one_hundred_thou_residents_all)
                VALUES(null, '{}', {}, {}, {}, {})
                    """.format(state_or_territory, total_correction_pop, total_correction_pop_per_one_hundred_thou_residents_all, total_pop_incarcerated, total_pop_incarcerated_per_one_hundred_thou_residents_all))

