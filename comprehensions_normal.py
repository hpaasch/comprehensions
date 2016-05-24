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

# Create a dictionary with the average wave height FOR EACH (WEEK?) DAY
# Step One: make a list of Sunday waves, Monday waves, etc.


# def avg_daily_wave_height():
    # wave_list = wave_timeline()

    #daily_waves = {}

    #sunday_waves = sum[]/5
    #monday_waves = sum[]/5
    #tuesday_waves = sum[]/4
    #wednesday_waves = sum[]/4
    #thursday_waves = sum[]/4
    #friday_waves = sum[]/4
    #saturday_waves = sum[]/5

    #total_waves = sum(floated_waves)
    #avg_wave = total_waves/len(wave_list)
    #print(avg_wave)
    #return avg_wave
# avg_wave_height()

def waves_per_day(): # this coding authored by Joel Taddei taddeimania
    from enum import Enum

    class DayOfWeek(Enum):
        Sunday = 0
        Monday = 1
        Tuesday = 2
        Wednesday = 3
        Thursday = 4
        Friday = 5
        Saturday = 6

    def get_day_of_week(year, month, day):
        month_table = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        year -= 1 if month < 3 else 0
        return DayOfWeek(int((year + year / 4 - year / 100 + year / 400 + month_table[month - 1] + day) % 7))

    print(get_day_of_week(1990, 4, 2))
    return get_day_of_week(1990, 4, 2)
# waves_per_day()

# Create a nested comprehension to get the average of the Homework 1 grades.


def homework_average():
    grade_dict = {
        'Gale': {'Homework 1': 88, 'Homework 2': 76},
        'Jordan': {'Homework 1': 92, 'Homework 2': 87},
        'Peyton': {'Homework 1': 84, 'Homework 2': 77},
        'River': {'Homework 1': 85, 'Homework 2': 91},
        }
    homework_one = []
    names = grade_dict.keys()

    for names in grade_dict:
        this = (grade_dict.get(names, {}).get('Homework 1'))
        homework_one.append(this)

    #one = (grade_dict.get(key, {}).get('Homework 1'))

    #homework = grade_dict.values()
    #homework_one = {'Homework 1': value for key, value in grade_dict.values()}


    # print(names)
    #print(homework)
    print(this)
homework_average()
# avg_homework_one = {header: input_set[index] for name, homework in enumerate(headers)}
