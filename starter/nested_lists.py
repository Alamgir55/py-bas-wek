couples = [
    ["Beyonce", "Jay-Z"],
    ["Johnny", "June"],
    ["John", "Yoko"],
    ["Will", "jada"]
]

for couple in couples:
    print(couple)
    for person in couple:
        print(f"Sending invite to....{person}")
