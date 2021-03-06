# The Birthday Paradox claims the there is a very high likeliness of having a matching birthday
# This programs test the likeliness using the Monte Carlos simulation model.

import datetime
import random

MAX_GENERATIONS = 100 # Maximum number of birthdays randomly generated
MAX_EXPERIMENTS = 1000 # Maximum number of samples to randomly generate

def getBDays(num_of_bdays: int) -> list:
    bdays = []

    for i in range(num_of_bdays):
        first_day_of_year = datetime.date(2021, 1, 1) # starts at the first day of the year

        # generates a random number of days to add to the first day of the year
        random_num_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = first_day_of_year + random_num_of_days
        bdays.append(birthday)
    return bdays


def checkMatch(birthdays: list) -> datetime or None:
    if len(birthdays) == len(set(birthdays)):
        return None # All birthday are unique

    # Iterates through birthdays comparing each birthday to the rest
    for i, bday1 in enumerate(birthdays):
        for j, bday2 in enumerate(birthdays[i + 1 :]):
            if bday1 == bday2:
                return bday1    # return the matching birthday

# Run a single iteration of the experiment
# returns 0 if a match is found
# returns 1 if no match is found
def runExperiment() -> int:
    # Generates birthdays
    birthdays = getBDays(num_of_bdays=num_of_bdays)

    # Checks if there are matches in birthdays
    match = checkMatch(birthdays=birthdays)

    # Displays results
    if match != None:
        return 0
    else:
        return 1

# list for converting month names
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


# Checks user input to be valid
while True:
    print('How many birthdays to generate (Max {}):'.format(MAX_GENERATIONS))
    response = input('> ')
    if response.isdigit() and (0 < int(response) <= MAX_GENERATIONS):
        num_of_bdays = int(response)
        break

while True:
    print('How many experiments to generate (Max {}):'.format(MAX_EXPERIMENTS))
    response = input('> ')
    if response.isdigit() and (0 < int(response) <= MAX_EXPERIMENTS):
        num_of_expts = int(response)
        break

print()
print('Here\'s a sample experiment')
# Generates birthdays
birthdays = getBDays(num_of_bdays=num_of_bdays)

# Displays the generated birthdays
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')

    month_name = MONTHS[birthday.month - 1]
    date_text = '{} {}'.format(month_name, birthday.day)
    print(date_text, end='')
print()

# Checks if there are matches in birthdays
match = checkMatch(birthdays=birthdays)


# Displays results
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = '{} {}'.format(month_name, match.day)
    print('In this simulation, multiple people had the same birthday on {}'.format(date_text))
else:
    print('In this simulation, there were not any matching birthdays')

print()

# Runs the requested number of experiments
passes = 0 # Tracks number of matches found
for x in range(num_of_expts):
    result = runExperiment()
    if result == 0:
        passes += 1
probablity = round(passes / num_of_expts * 100, 2) # calculates percentage of matched experiments

# Displays the results
print('Out of {} experiments, each with {} number of people'.format(num_of_expts, num_of_bdays))
print('A total of {} experiments had at least two people with matching birthdays'.format(passes))
print('That\'s a probability of {}%'.format(probablity))