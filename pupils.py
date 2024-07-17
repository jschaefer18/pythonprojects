import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    student_list = read_compound_list('pupils.csv')
    extract_birthday = lambda student: student[BIRTHDATE_INDEX]
    sorted_list = sorted(student_list, key=extract_birthday)
    print_list(sorted_list)

    



def read_compound_list(filename):
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            compound_list.append(row)

    return compound_list


def print_list(compound_list):
    for element in compound_list:
        print(element)
    print()


if __name__ == "__main__":
    main()
