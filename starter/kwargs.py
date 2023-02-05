# def demo(**kwargs):
#     print(kwargs)


# def display_info(person,status="single", *args):
#     print(f"person is: {person}")
#     print(f"status is: {status}")
#     print(f"args is: {args}")

# def add_thrice(val, lst=[]):
#     lst.append(val)
#     lst.append(val)
#     lst.append(val)
#     return lst

# def add_thrice(val, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(val)
#     lst.append(val)
#     return lst

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total
