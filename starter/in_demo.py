flavors = ["chocolate", "vanilla", "lemon", "strawberry"]

response = input("What flavor would you like?")

while response.lower() not in flavors:
    response = input("i don't know that flavor! Try again:")

print(flavors.count("chocolate"))

print(f"Ok, {response} ice cream coming right up!")
