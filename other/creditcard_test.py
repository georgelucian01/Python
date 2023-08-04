
def test_creditcard(number):

    # step 1
    number.replace('-', '')
    number.replace(' ', '')

    number = number[::-1]
    sum_odd_digits = 0
    sum_even_digits = 0
    
    # step 2
    for x in number[::2]:
        sum_odd_digits += int(x)

    # step 3
    for x in number[1::2]:
        double = int(x) * 2
        if double < 10:
            sum_even_digits += double
        else:
            sum_even_digits += (1 + double%10)

    total = sum_odd_digits + sum_even_digits

    if total % 10 == 0:
        return 'Valid'
    
    return "Invalid"

def main(): 
    creditcard = input("Enter a credit card number = ")
    print(test_creditcard(creditcard))
 
if __name__ == "__main__":
    main()