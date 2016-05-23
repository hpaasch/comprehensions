# -----------------------------------
# Remove all vowels from the sentence

def flabby_loop_vowels():
    text = "List Comprehensions are the Greatest!"
    vowels = ("a", "e", "i", "o", "u")

    for letter in text:
        if letter in vowels:
            text = text.replace(letter, "")
    # print(text)
    return text
flabby_loop_vowels()

def svelte_comprehension_vowels():
    text = "List Comprehensions are the Greatest!"
    vowels = ("a", "e", "i", "o", "u")
    text = [letter for letter in text if letter not in vowels]
    new_text = "".join(text)
    # print(new_text)
    return new_text
svelte_comprehension_vowels()

# ------------------------------------------------------------
# BONUS: Create open_and_extract function that will generate a list on whatever column I want.
# water_temp, water_date, wave_height




# ------------------------------------------------------------
# Create a list of Water Temps for each day the data set below.

def collect_water():
    import csv
    with open("data_set.txt") as water_data:
        read_water_data = csv.reader(water_data, delimiter=',')
        next(read_water_data, None)
        water_temps = []

        for row in read_water_data: # change to comprehension
            water_temp = row[-2]
            water_temps.append(water_temp)
        # print(water_temps)
        return water_temps
collect_water()

def collect_dates():
    import csv
    with open("data_set.txt") as water_data:
        read_water_data = csv.reader(water_data, delimiter=',')
        next(read_water_data, None) # skips the header
        dates = []

        for row in read_water_data: # change to comprehension
            date = row[-1]
            dates.append(date)
        # print(dates)
        return dates
collect_dates()

# ------------------------------------------------
# Convert the Water Temps from a string to a float

def float_those_temperatures():
    floated_water_temps = []

    for temperature in collect_water():  # change to comprehension
            floated_temp = float(temperature)
            floated_water_temps.append(floated_temp)

    # print(floated_water_temps)
    return floated_water_temps
float_those_temperatures()


# Convert the Water Temps from Celsius to Fahrenheit rounded to an int

def convert_temps():
    farenheit_water_temps =[]

    for item in float_those_temperatures(): # change to comprehension
        conversion_temp = int((item * 1.8) + 32)
        farenheit_water_temps.append(conversion_temp)
    # print(farenheit_water_temps)
    return farenheit_water_temps
convert_temps()

# --------------------------------------------------------------------
# Create a dictionary with Date as the key and Wave Height as the value
# Step One: create list of Wave Height

def collect_waves():
    waves = {}
    import csv
    with open("data_set.txt") as water_data:
        read_water_data = csv.reader(water_data, delimiter=',')
        next(read_water_data, None)  # skips the header
        wave_list = []

        for row in read_water_data:  # change to comprehension
            wave_temp = row[1]
            wave_list.append(wave_temp)
    # print(wave_list)
    return wave_list
collect_waves()

# Step Two: Marry collect_waves with collect_dates in a dictionary
def wave_timeline():
    

# Create a dictionary with the average wave height for each day

