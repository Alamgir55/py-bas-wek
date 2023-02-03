lando_2021_results = [2, 5, 56, 45, 4124, 545, 24, 4, 5, 6, 2, 1, 5]

total = 0
for num in lando_2021_results:
    total += num

    # print(total)


def average(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)


min = lando_2021_results[0]
for num in lando_2021_results:
    if num < min:
        min = num

print(min)
