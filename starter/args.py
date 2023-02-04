# def count_stuff(*args):
#     print(args)

# def count_stuff(*args):
#     print(f"You pass me {len(args)} arguments")

# def sum(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

def silly(first, second, *other):
    print(f"first is: {first}")
    print(f"second is  {second}")
    print(f"others is {other}")
