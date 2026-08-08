# Mutability and Immutability

# Notes
"""
Everything is an object in python.

And every object has following attributes
    -> identity (ALWAYS USE to check if it's mutable/immutable)
            * If the identity is the same, that means the object is immuatable (we are getting the same object) otherwise mutable.
    -> type
    -> value (NEVER check with value for mutability/immutability)
            * Value can/cannot be same even if identity is different.

There are two types of objects.
  1) Mutable - Once created, can be changed later. (changeable)
  2) Immutable - Once created, CANNOT be changed later. Can assign new references, but old reference remains unchanged. (NOT changeable)
"""

age = 18 # Ephemeral int storage (int variable) [This is actually immutable]
print(f'My age is {age}')
print(f'ID of 18 = {id(18)}')
print(f'ID of age = {id(age)}')


age = 20 # This time we changed the reference that once pointed to the memory location which contained value 18, to now point to 20
print(f'My age is changed to {age}')
print(f'ID of 20 = {id(20)}')
print(f'ID of age = {id(age)}')
