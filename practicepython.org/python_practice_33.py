
## July 28th 2023
## Problem number 33
## https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

# dictionary with birthdays
birthdays = {'Albert Einstein': 'March 14, 1879',
            'Benjamin Franklin' : 'January 17, 1706',
            'Ada Lovelace': 'December 10, 1815',
            'George Lucian': 'November 23, 1999',
            'Bianca Elena': 'October 31, 2002'}

# Main
def main():
    
    name = input("Who's birthday do you want to look up?\n")
    print(name + "'s birthday is " + birthdays.get(name)+ ".")

# Run main()
if __name__ == "__main__":
    main()
