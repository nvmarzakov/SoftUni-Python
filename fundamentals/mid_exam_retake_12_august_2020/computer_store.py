CUSTOMER_TYPES = {1: 'regular', 2: 'special',
}
total_price_bf_taxes = 0
customer_type = ''
while True:
    command = input()
    if command == CUSTOMER_TYPES[1] or command == CUSTOMER_TYPES[2]:
        customer_type += command
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue
    total_price_bf_taxes += price
if total_price_bf_taxes == 0:
    print("Invalid order!")
else:
    taxes = total_price_bf_taxes * 0.2
    final_price = total_price_bf_taxes + taxes
    if customer_type == 'special':
        final_price *= 0.9
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_bf_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
