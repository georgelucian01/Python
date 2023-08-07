# args kwargs

def add(a, b):
    return a + b

print(add(10, 15))

def add2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add2(1, 2, 10, 100, 25))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("George", "Lucian", "The Third")


def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    

print_adress(street="Strada Tuela",
            apt = "25",
            city="Brasov",
            zipcode="123457")


def shipping_label(*args, **kwargs):
    print("We are shipping to: ", end="")
    for arg in args:
        print(arg, end=" ")
    print()

    print("Address is: ")
    for key, value in kwargs.items():
        print(f"{key} : {value}")


shipping_label("Dr", "George", "Lucian", "III",
                country = "Bulgaria", city= "Sofia", street= "Saint Peter 23")
