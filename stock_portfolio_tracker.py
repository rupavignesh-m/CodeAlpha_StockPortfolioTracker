# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 140,
    "MSFT": 320
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

num = int(input("Enter number of stocks you own: "))

for i in range(num):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total += investment
        print("Investment in", stock, "=", investment)
    else:
        print("Stock not available.")

print("\nTotal Investment Value = $", total)

# Save result to a text file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = $" + str(total))
file.close()

print("Result saved to portfolio.txt")
