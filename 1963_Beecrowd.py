x, y = input('').split()
old_price = float(x)
new_price = float(y)

z = (new_price/old_price - 1) * 100
print(f'HOW ABSURD! THE PRICE OF CINEMA TICKETS HAS RISEN {z:.2f} %!!')


