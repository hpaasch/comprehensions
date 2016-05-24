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
        water_temps = [row[-2] for row in read_water_data]
        # print(water_temps)
        return water_temps
collect_water()


def collect_dates():
    import csv
    with open("data_set.txt") as water_data:
        read_water_data = csv.reader(water_data, delimiter=',')
        next(read_water_data, None)  # skips the header
        dates = [row[-1] for row in read_water_data]
        # print(dates)
        return dates
collect_dates()

# ------------------------------------------------
# Convert the Water Temps from a string to a float


def float_those_temperatures():
    unfloated_water = collect_water()
    floated_water_temps = [float(temperature) for temperature in unfloated_water]
    # print(floated_water_temps)
    return floated_water_temps
float_those_temperatures()


# Convert the Water Temps from Celsius to Fahrenheit rounded to an int

def convert_temps():
    floated_temps = float_those_temperatures()
    farenheit_water_temps =[int(item * 1.8 + 32) for item in floated_temps]
    # print(farenheit_water_temps)
    return farenheit_water_temps
convert_temps()

# --------------------------------------------------------------------
# Create a dictionary with Date as the key and Wave Height as the value
# Step One: create list of Wave Height


def collect_waves():
    import csv
    with open("data_set.txt") as water_data:
        read_water_data = csv.reader(water_data, delimiter=',')
        next(read_water_data, None)  # skips the header
        wave_list = [row[1] for row in read_water_data]
    # print(wave_list)
    return wave_list
collect_waves()

# Step Two: Marry collect_waves with collect_dates in a dictionary


def wave_timeline():
    date_list = collect_dates()
    wave_list = collect_waves()

    waves = dict(zip(date_list, wave_list))
    # print(waves)
    return waves
wave_timeline()

# Create a dictionary with the average wave height for each day


def avg_wave_height():
    wave_list = (collect_waves())
    avg_wave = sum(wave for wave in wave_list if wave)/len(wave_list)
    print(avg_wave)
# avg_wave_height()


# Create a nested comprehension to get the average of the Homework 1 grades.
