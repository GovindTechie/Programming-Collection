def calculate_total_cost():
    tickets = int(input("Enter the number of tickets:\n"))
    refreshment = input("Do you want refreshment? (y/n):\n").lower()
    coupon = input("Do you have a coupon code? (y/n):\n").lower()
    ticket_class = input("Enter the class type (k/q):\n").lower()

    if tickets < 5:
        print("Minimum of 5 tickets must be booked")
        return

    price_per_ticket = 75 if ticket_class == 'k' else 150
    base_cost = tickets * price_per_ticket

    if tickets > 20:
        base_cost *= 0.90

    if coupon == 'y':
        base_cost *= 0.98

    if refreshment == 'y':
        base_cost += tickets * 50

    print(f"Total ticket cost: Rs.{base_cost:.2f}")

calculate_total_cost()
