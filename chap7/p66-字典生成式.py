items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]

# d = {item:price for item, price in zip(items, prices) }
d = {item.upper():price for item, price in zip(items, prices) }
print(d)