stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 120
}

portfolio = {}
total_value = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))


while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid input. Please enter a number.")


print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")


save = input("Would you like to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (e.g., portfolio.txt): ")
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print(f"Portfolio saved to '{filename}'")
