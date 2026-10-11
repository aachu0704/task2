
import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = []
total_investment = 0

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price} per share")

print("\nEnter the stocks you want to invest in.")

try:
    number_of_stocks = int(
        input("\nHow many different stocks do you want to buy? ")
    )

    if number_of_stocks <= 0:
        print("Please enter a number greater than zero.")
    else:
        for i in range(number_of_stocks):
            print(f"\nStock {i + 1}")

            stock_name = input(
                "Enter stock symbol: "
            ).strip().upper()

            if stock_name not in stock_prices:
                print("Stock not available. Skipping this entry.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            price = stock_prices[stock_name]
            investment = price * quantity

            portfolio.append({
                "Stock": stock_name,
                "Price": price,
                "Quantity": quantity,
                "Investment": investment
            })

            total_investment += investment

        print("\n" + "=" * 40)
        print("          PORTFOLIO SUMMARY")
        print("=" * 40)

        if portfolio:
            print(f"{'Stock':<10}{'Price':<10}"
                  f"{'Quantity':<10}{'Total':<10}")

            for item in portfolio:
                print(
                    f"{item['Stock']:<10}"
                    f"${item['Price']:<9}"
                    f"{item['Quantity']:<10}"
                    f"${item['Investment']:<10}"
                )

            print("-" * 40)
            print(f"Total investment: ${total_investment}")

            save = input(
                "\nSave portfolio to CSV? (yes/no): "
            ).strip().lower()

            if save in ("yes", "y"):
                with open(
                    "portfolio.csv", "w", newline=""
                ) as file:
                    writer = csv.DictWriter(
                        file,
                        fieldnames=[
                            "Stock", "Price",
                            "Quantity", "Investment"
                        ]
                    )
                    writer.writeheader()
                    writer.writerows(portfolio)

                print("Portfolio saved to portfolio.csv")
        else:
            print("No valid stocks were entered.")

except ValueError:
    print("Invalid input. Please enter numbers for quantity.")
    
print("\nThank you for using Stock Portfolio Tracker!")

