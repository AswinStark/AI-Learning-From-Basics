# Tuples are Pairs in Python.

my_hobbies_interest = [("coding", 5), ("reading", 5), ("painting", 5), ("Video Games", 3), ("Trips", 5), ("Movies", 5), ("Cooking", 4), ("Cleaning", 2)]

print(f"\nBefore Applying lower operation:\n")
for hobby, rating in my_hobbies_interest:
    print(hobby, end=",")

print("\nApplying lower operation on the elements:")
for hobby, rating in my_hobbies_interest:
    hobby = hobby.lower()

# Performing membership operation in list of tuple
hobby = input("Enter the hobby with rating 5: ").lower()

if (hobby,5) in my_hobbies_interest:
    print(f"Hobby found with rating 5")