# def outer():
#     animal = "Secretary Bird"

#     def inner():
#         print("INSIDE INNER FUNC ", animal)

#         def third():
#             print("third INNER FUNC ", animal)

#         third()
#     inner()


# outer()

# def outer():
#     global animal
#     animal = "Spider Crab"


# outer()

# print(animal)

score = 100


def double_score():
    global score
    score = score * 2


double_score()
print(score)
