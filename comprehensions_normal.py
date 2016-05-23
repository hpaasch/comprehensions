# -----------------------------------
# Remove all vowels from the sentence

# with a flabby FOR loop
text = "List Comprehensions are the Greatest!"
vowels = ("a", "e", "i", "o", "u")

for letter in text:
    if letter in vowels:
        text = text.replace(letter, "")
print(text)

# with a svelte List Comprehension
text = "List Comprehensions are the Greatest!"
vowels = ("a", "e", "i", "o", "u")
text = [letter for letter in text if letter not in vowels]
print("".join(text))

# ------------------------------------------------------------
# Create a list of Water Temps for each day the data set below.

import csv
with open("data_set.txt") as water_data:
    read_water_data = csv.reader(water_data, delimiter=',')
    next(read_water_data, None)
    dates = []
    water_temps = []

    for row in read_water_data:
        date = row[-1]
        water_temp = row[-2]
        dates.append(date)
        water_temps.append(water_temp)
    print(dates)
    print(water_temps)

# ------------------------------------------------
# Convert the Water Temps from a string to a float
    floated_water_temps = []

    for temperature in water_temps:
            floated_temp = float(temperature)
            floated_water_temps.append(floated_temp)
    print(floated_water_temps)


# Convert the Water Temps from Celsius to Fahrenheit rounded to an int
# Create a dictionary with Date as the key and Wave Height as the value
# Create a dictionary with the average wave height for each day

