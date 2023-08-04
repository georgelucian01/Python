
## July 27th 2023
## Problem number 22
## https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

## Count how many times a name is in txt file
## Print results

# for names
def count_similar_names(file): 
    # using hash table/dictionary
    name_count = {}

    with open(f'{file}.txt', 'r') as read_file:
        for line in read_file:
            line = line.strip()
            name_count[line] = name_count.get(line, 0) + 1
    return name_count

# Extra
# for categories
def count_categories(file):
    cat_count = {}

    with open(f'{file}.txt','r') as read_file:
        for line in read_file:
            line.strip()
            cat = extract_middle_part(line)
            cat_count[cat] = cat_count.get(cat, 0) + 1
    return cat_count
 
def extract_middle_part(line):
    parts = line.split('/')
    return parts[2]

def main():
    # names.txt
    print(count_similar_names("names"))
    # categories.txt
    print(count_categories("categories"))

if __name__ == "__main__":
    main()


