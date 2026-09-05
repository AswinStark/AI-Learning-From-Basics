choice = input("Please enter your flavour preference (Vanilla/Hazelnut/Nuttela): ").lower()

if choice == "vanilla":
    print(f"Great choice! Here's your {choice} icecream")
elif choice == "hazelnut":
    print(f"Nice one! Here's your {choice} icecream")
elif choice == "nuttela":
    print(f"You are one of a kind going ahead with not so popular {choice} icecream!")
else:
    print("Invalid icecream flavour!!")