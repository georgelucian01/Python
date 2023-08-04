
## July 27th 2023
## Problem number 23
## https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

## Given two text files find the numbers that are overlapping

# Transforms a file into a list
def txt_to_list(file):
    with open(f'{file}.txt', 'r') as read_file:
        new_list = list(read_file.read().split('\n'))
    return new_list

# Find duplicates (insersection between lists) and returns them
def find_duplicates(file1, file2):
    list1 = txt_to_list(file1)
    list2 = txt_to_list(file2)
    list3 = [elem for elem in list1 if elem in list2]
    return list3
        
# Main        
def main():
    file1 = "primes"
    file2 = "happy_nums"
    print(find_duplicates(file1, file2))

# Run Main
if __name__ == "__main__":
    main()

