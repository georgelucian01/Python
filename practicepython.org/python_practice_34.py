
## July 31st 2023
## Problem number 34
## https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

import json

def write_to_json(file, content):
    
    try:
        with open(file, 'r') as json_file:
            existing_info = json.load(json_file)
    except FileNotFoundError:
        with open(file, 'w') as json_file:
            json.dump({}, json_file)
        existing_info = {}
    
    existing_info.update(content)

    with open(file, 'w') as json_file:
        json.dump(existing_info, json_file, indent=4)

def read_from_json(file):

    with open(file, 'r') as json_file:
        return json.load(json_file)

def create_dic(dictionary):
    print('Write "exit" to quit')
    while True:
        name = input("Name: ")

        if name.lower() == 'exit':
            return dictionary
        
        date = input("Date: ")
        
        dictionary[name] = date

# Main
def main():

    content = {
    "name": "Michele",
    "shirt_color": "blue",
    "laptops": [
    {
        "brand": "Lenovo",
        "operating_system": "Ubuntu"
    },
    {
        "brand": "Apple",
        "operating_system": "OSX"
    }
    ],
    "has_a_dog": False,
    "items_on_desk": ["mug", "pen", "monitor"]
}
    
    write_to_json('info.json', content)

    scientists = {}
    print(create_dic(scientists))
    write_to_json('info.json', scientists)
    

    info = read_from_json('info.json')

    print(info["name"])

    if info['has_a_dog']:
        print("{} has a dog".format(info['name']))
    else:
        print("{} doesn't have a dog".format(info['name']))
    
    print(info)

# Run main()
if __name__ == "__main__":
    main()
