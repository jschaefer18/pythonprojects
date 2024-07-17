import csv
def main():
  I_NUMBER_INDEX = 0
  NAME_INDEX = 1
  file = 'students.csv'
  dictionary = read_dictionary(file,0)
  i_number = input("Please enter an I-Number (xx-xxx-xxxx): ")
  i_number  = i_number.replace('-','')
  if not i_number.isdigit():
    print('Invalid I-Number')
  else:
    if len(i_number) < 9:
      print('I-Number too short')
    elif len(i_number) > 9:
      print('I-Number too long')
    else:
        if i_number not in dictionary:
          print('No such student')
        else:
          value = dictionary[i_number]
          name = value[NAME_INDEX]
          print(name)

  



def read_dictionary(filename,key_column_index):
   dictionary = {}
   with open(filename) as file:
    reader = csv.reader(file)
    next(file, 'rt')
    for row_list in reader:
      key = row_list[key_column_index]
      dictionary[key] = row_list
    return dictionary



main()

if __name__ == "__main__":
    main()