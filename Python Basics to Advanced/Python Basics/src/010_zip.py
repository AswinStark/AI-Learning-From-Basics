fruits = ["Apple", "Mango", "Pineapple", "Custard Apple", "Banana"]
prices = [120, 180, 100, 120, 70]

# zip allows us to iterate over multiple lists in one pass

for fruit, price in zip(fruits, prices):
    print(f"Fruit {fruit} costs {price}")