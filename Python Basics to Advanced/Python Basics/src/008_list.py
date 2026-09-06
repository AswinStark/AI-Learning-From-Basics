def separator_line(ch):
    return ""+ch * 100 + "\n"

currencies = ["INR", "USD", "YEN", "DINAR", "BITCOIN"]

print(f"Currency list: {currencies}")
print(f"Length of list: {len(currencies)}")

few_other_currencies = ["Australian Dollar", "EURO"]

currencies.append(few_other_currencies) # Adding like this adds as a list within a list

print(f"NEW Currency list after appending: {currencies}")
print(f"Length of currency list after appending: {len(currencies)}")

print(separator_line("_"))
print(f"\nRemoving last element {currencies[len(currencies)-1]} from currencies list")
currencies.pop(len(currencies)-1)

print(f"\nAfter Removing, state of currencies list: {currencies}")
print(f"NEW Currency list after removing: {currencies}")

print(separator_line("_"))

currencies.extend(few_other_currencies)
print(f"\nNEW Currency list aftrer extending: {currencies}")
print(f"Length of currency list after extending: {len(currencies)}")
print(separator_line("_"))
print(f"\n\nIterating List after extending:\n")
for curr in currencies:
    print(f"Availabe currency: {curr}")

#for i in range(0, currencies.__len__):

