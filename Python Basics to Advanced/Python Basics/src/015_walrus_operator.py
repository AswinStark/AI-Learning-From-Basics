# value =13
# remainder = value%5

# if remainder:
#     print(f"Not divisible, remainder = {remainder}")

# Example 1:
# WALRUS operator allows us to assign a larger expression to a variable in a if statement
value = 13
if (remainder := value % 5):
    print(f"Not divisible, remainder = {remainder}")

# Example 2:

available_fruits = ["Apple", "Mango", "Watermelon", "MuskMelon", "Pineapple", "Orange"]

if(requested_fruit := input(("Enter needed fruit: "))) in available_fruits:
    print(f"{requested_fruit} is available")
else:
    print(f"{requested_fruit} is not available.")

# Example 3
while (fruit := input("Enter fruit: ")) not in available_fruits:
    print(f"{fruit} is not available!")

print(f'{fruit} is available')