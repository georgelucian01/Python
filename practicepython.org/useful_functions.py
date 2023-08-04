class functions:
    
    ## Ask for int input
    def int_input():
        while True:
            try:
                user_input = input("Enter an integer: ")
                number = int(user_input)
                return number
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def int_input_msg(message):
        while True:
            try:
                user_input = input(message)
                number = int(user_input)
                return number
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    ## Ask for int input of x digits
    def int_input_x_digit(x):
        while True:
            num_str = input(f"Enter a {x} digit number: ")
            if len(num_str) != x:
                print("Enter valid number!")
                continue
            try:
                num = int(num_str)
                break
            except ValueError:
                print("Enter valid number!")
        return num

    ## Generate random list of numbers
    def random_list_of_ints(range_of_nums, size_of_list):
        if size_of_list > range_of_nums:
            print("Size larger than range")
            return 0
        import random

        list = random.sample(range(range_of_nums), size_of_list)
        print(list)
        return list
    
    

