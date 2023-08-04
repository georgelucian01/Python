
## July 31st 2023
## Problem number 35
## https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html

## Get the count of months from the json file

import json
from collections import Counter


# Read Json
def read_from_json(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)

# Main
def main():

    json_file = read_from_json('info.json')
    months_of_year = read_from_json('months.json')
    
    # Get the dates and put them in list
    dates = list(json_file.values())
    months = []

    for month in dates:
        value = month.split('/')[1]
        months.append(value)

    months.sort()

    month_names = []

    for m in months:
        n = months_of_year.get(m)
        month_names.append(n)
    
    c = Counter(month_names)
    
    print(c)
    


# Run main()
if __name__ == "__main__":
    main()
