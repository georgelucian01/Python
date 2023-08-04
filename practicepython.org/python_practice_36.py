
## July 31st 2023
## Problem number 36
## https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html


import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

def get_months(file):

    json_file = read_from_json(file)
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

    return c

# Read Json
def read_from_json(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)

# Main
def main():
    data = get_months('info.json')
    print(data)

    # HTML file where the output will go
    output_file('months_graph.html')

    # load x and y data
    # get biggest value
    max_value = max(data.values())

    x = [x for x in data.keys()]
    y = [y for y in data.values()]
    
    # create figure
    p = figure(x_range=x)

    # create a histrogram
    p.vbar(x=x, top=y, width=0.5)

    # render the plot
    show(p)

# Run main()
if __name__ == "__main__":
    main()
