
# create a cart, add items and calculate the total


import os
import time


def print_dct(dct, pos2, um):
    print("Items:")
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print(f"{item}, {pos2}: {amount} {um}")

def main(): 

    menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

    cart = {}
    
    stop = False
    while True:
        print("----------------")
        print_dct(menu, 'pret', 'EUR')
        print("----------------")
        # Adaugare cart
        while True:
            buy = input("What do you to buy? (exit to quit) ")
            if buy == 'exit':
                stop = True
                break
            if buy not in menu.keys():
                buy = input("What do you to buy? (exit to quit) ")
                if buy == 'exit':
                    stop = True
                    break
            break

        if stop:
            break

        q = input("How many do you want? ")
        print("----------------")
        print(f'Ok, you will have {buy}, quantity {q} pcs.')
        print("----------------")
        time.sleep(2)

        # clear terminal
        os.system('cls')

        # check if item is already in cart and add more quantity if its the case
        if buy in cart:
            cart[buy] += int(q)
        else:
            cart[buy] = int(q)
    
    
    total = 0
    
    for item, quant in cart.items():
        total += (menu[item] * quant)
    print("----------------")
    print_dct(cart, 'cantitate', 'buc')
    print("----------------")
    print(f"Total: {total} {'EUR'}")

if __name__ == "__main__":
    main()