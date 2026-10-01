fruit_prices = {
    "Apple" : {"price":120, "state":"Sour-Sweet"},
    "Mango": {"price":130, "state":"Sweet"},
    "Pineapple": {"price":100, "state":"Unripe"}
}

# Ways to access dictionary
print(f"Apple details: {fruit_prices.get("Apple")}")

print(f"Apple state: {fruit_prices["Apple"]["state"]}")

for fruit, details in fruit_prices.items():
    print(f"{fruit} costs {details["price"]}")
