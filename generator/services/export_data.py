import csv

from generator.constants.function_generator_dict import FUNCTIONS_DICT


def generate_csv(rows_num, columns):
    """
    Generation CSV File
    Parameters
    ----------
    rows_num : int
    columns : QuerySet
    """
    sorted_array = sorted([item for item in columns], key=lambda x: x.order)

    with open('data_set.csv', mode='w', newline='') as data_set_file:
        writer = csv.writer(data_set_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([item.name for item in sorted_array])
        for _ in range(rows_num):
            writer.writerow([FUNCTIONS_DICT[item.type](item.start_from, item.to) for item in sorted_array])

    data_set_file.close()
