# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: RON "))
        foods.append(food)
        prices.append(price)


## branch test


print("----- Cart -----")
for food in foods:
    print(food, end=" ")


for price in prices:
    total += price

print(f"\nTotal: {total}")
print("----------------")