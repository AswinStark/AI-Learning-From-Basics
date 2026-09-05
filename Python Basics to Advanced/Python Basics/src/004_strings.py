# STRINGS
first_name = "Aswin"
last_name = "Stark"

full_name = first_name + " " + last_name

print(f"Full name is {full_name}")

# While working with strings it is important to make sure to encode the string before transmitting. The receiving end should decode it back.
encoded_string = "Aswin@qualcomm.company.com".encode(encoding = "utf-8")

print(f"Encoded String: {encoded_string}")

decoded_string = encoded_string.decode(encoding = "utf-8")

print(f"Decoded String = {decoded_string}")

# String Functions
lower_case_full_name = full_name.lower()

print(f"Lower case: {lower_case_full_name}")