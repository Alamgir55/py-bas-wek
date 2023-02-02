# def laugh(strength=2):
#     print("HA" * strength)


# laugh(10)
# laugh()

def slugify(phrase, sep="-"):
    return phrase.lower().strip().replace(" ", sep)


print(slugify("hello world chicken face", "_"))
