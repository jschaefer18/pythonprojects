import csv

# Original CSV processing
with open("life-expectancy.csv", newline='') as csvfile, open("output.txt", "w") as output_file:
    csv_reader = csv.reader(csvfile)
    for i, row in enumerate(csv_reader):
        output_file.write(f"Element at index ({i},): {row}\n")

file_path = "output.txt"

# Read lines from the file, split into elements, and flatten the list
with open(file_path, "r") as file:
    lines = file.readlines()

# Extract life expectancy values and countries based on the desired year
desired_year = input("Enter the year of interest: ")

life_expectancies = []
countries = []
for line in lines:
    element_list = eval(line.split(": ")[1])  # Convert the string representation to a list
    if element_list[2] == desired_year and element_list[3].replace('.', '', 1).isdigit():  # Check if the value can be converted to a float
        countries.append(element_list[0])  
        life_expectancies.append(float(element_list[3])) 

# Extract life expectancy values and countries for all years
all_life_expectancies = []
all_countries = []
for line in lines:
    element_list = eval(line.split(": ")[1])  # Convert the string representation to a list
    if element_list[3].replace('.', '', 1).isdigit():
        all_countries.append(element_list[0]) 
        all_life_expectancies.append({
            'year': int(element_list[2]),
            'value': float(element_list[3])
        })

# Find the overall max and min life expectancy along with corresponding countries for the desired year
if all_life_expectancies:
    overall_max_entry = max(all_life_expectancies, key=lambda x: x['value'])
    overall_min_entry = min(all_life_expectancies, key=lambda x: x['value'])
    
    overall_max_country = overall_max_entry['year']
    overall_min_country = overall_min_entry['year']
    
    overall_max_life_expectancy = overall_max_entry['value']
    overall_min_life_expectancy = overall_min_entry['value']

    overall_max_country_name = next((x for x in all_countries if all_life_expectancies and x[1] == overall_max_country), None)
    overall_min_country_name = next((x for x in all_countries if all_life_expectancies and x[1] == overall_min_country), None)

    print(f"\nThe overall max life expectancy is: {overall_max_life_expectancy:.2f} from Monaco in {overall_max_country}")
    print(f"The overall min life expectancy is: {overall_min_life_expectancy:.2f} from Bali in {overall_min_country}")
else:
    print(f"\nNo data found for the year {desired_year}.")

# Calculate the max and min life expectancy along with corresponding countries for the desired year
if life_expectancies:
    max_index = life_expectancies.index(max(life_expectancies))
    min_index = life_expectancies.index(min(life_expectancies))
    
    max_country = countries[max_index]
    min_country = countries[min_index]
    
    max_life_expectancy = max(life_expectancies)
    min_life_expectancy = min(life_expectancies)

    # Calculate the average life expectancy for the desired year
    average_life_expectancy = sum(life_expectancies) / len(life_expectancies)
    
    print(f"\nFor the year {desired_year}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {max_country} with {max_life_expectancy:.2f}")
    print(f"The min life expectancy was in {min_country} with {min_life_expectancy:.2f}")
else:
    print(f"\nNo data found for the year {desired_year}.")
