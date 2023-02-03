def get_total(price, qty=1, tax=0.02, discount=0):
    subtotal = price * qty * (1-discount)
    print(subtotal * (1 + tax))


# get_total(4.99, 5, 0.015, 0.2)

get_total(tax=0.20, qty=5, price=9.58, discount=0.5)
