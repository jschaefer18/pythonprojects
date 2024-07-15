def c_to_f(x):
    temp = (x * 9/5) + 32
    return temp

def calculate_windchill(t, v):
    windchill = 35.74 + 0.621 * t - 35.75 * (v**0.16) + 0.4275 * t * (v**0.16)
    return windchill

while True:
    v = 5
    try:
        temp = float(input("What is the temperature? "))
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for temperature.")
        continue

    measurement = input("Fahrenheit or Celsius (F/C)? ")
    if measurement.upper() == "C":
        new_temp = c_to_f(temp)
        while v <= 60:
            term = calculate_windchill(new_temp, v)
            print(f"At temperature {new_temp:.2f}F, and wind speed {v} mph, the windchill is: {term:.2f}")
            v = v + 5
    elif measurement.upper() == "F":
        while v <= 60:
            term = calculate_windchill(temp, v)
            print(f"At temperature {temp:.2f}F, and wind speed {v} mph, the windchill is: {term:.2f}")
            v = v + 5
