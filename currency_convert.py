# Currency Conversion Program
# Author: [Your Name]
# Date: [Today's Date]

# Exchange rates table
exchange_rates = {
    'CAD': {'CAD': 1.0000, 'USD': 1.3118, 'EUR': 1.4983, 'GBP': 1.6832, 'JPY': 0.0117, 'CNY': 0.1890, 'CHF': 1.3160, 'INR': 0.0179},
    'USD': {'CAD': 0.7625, 'USD': 1.0000, 'EUR': 1.1417, 'GBP': 1.2829, 'JPY': 0.0089, 'CNY': 0.1440, 'CHF': 1.0029, 'INR': 0.0137},
    'EUR': {'CAD': 0.6681, 'USD': 0.8761, 'EUR': 1.0000, 'GBP': 1.1237, 'JPY': 0.0078, 'CNY': 0.1261, 'CHF': 0.8783, 'INR': 0.0120},
    'GBP': {'CAD': 0.5944, 'USD': 0.7796, 'EUR': 0.8900, 'GBP': 1.0000, 'JPY': 0.0070, 'CNY': 0.1123, 'CHF': 0.7818, 'INR': 0.0107},
    'JPY': {'CAD': 85.2902, 'USD': 111.8642, 'EUR': 127.7273, 'GBP': 143.5219, 'JPY': 1.0000, 'CNY': 16.1130, 'CHF': 112.1951, 'INR': 1.5301},
    'CNY': {'CAD': 5.2936, 'USD': 6.9430, 'EUR': 7.9270, 'GBP': 8.9068, 'JPY': 0.0621, 'CNY': 1.0000, 'CHF': 6.9630, 'INR': 0.0950},
    'CHF': {'CAD': 0.7604, 'USD': 0.9971, 'EUR': 1.1384, 'GBP': 1.2792, 'JPY': 0.0089, 'CNY': 0.1436, 'CHF': 1.0000, 'INR': 0.0136},
    'INR': {'CAD': 55.7528, 'USD': 73.1157, 'EUR': 83.4803, 'GBP': 93.8001, 'JPY': 0.6536, 'CNY': 10.5313, 'CHF': 73.3300, 'INR': 1.0000}
}

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency):
    # Check if the currencies are in the exchange rates table
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        # Get the exchange rate
        rate = exchange_rates[from_currency][to_currency]
        # Calculate the converted amount
        converted_amount = amount * rate
        return converted_amount
    else:
        # Return None if the conversion is not possible
        return None

# Main program
def main():
    # Display welcome message
    print("Welcome to the Currency Converter!")
    
    # Main loop to allow multiple conversions
    while True:
        # Display menu options
        print("\nPlease select the conversion you'd like to perform:")
        print("1. JPY to USD")
        print("2. EUR to GBP")
        print("3. INR to CNY")
        print("4. CAD to CHF")
        print("5. Exit")
        
        # Get user's choice
        choice = input("Enter your choice: ")
        
        # Set the source and target currencies based on the user's choice
        if choice == '1':
            from_currency = 'JPY'
            to_currency = 'USD'
        elif choice == '2':
            from_currency = 'EUR'
            to_currency = 'GBP'
        elif choice == '3':
            from_currency = 'INR'
            to_currency = 'CNY'
        elif choice == '4':
            from_currency = 'CAD'
            to_currency = 'CHF'
        elif choice == '5':
            # Exit the program if the user chooses option 5
            print("Thank you for using the Currency Converter!")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")
            continue
        
        # Get the amount to convert
        amount = float(input(f"Enter the amount in {from_currency}: "))
        
        # Perform the conversion
        converted_amount = convert_currency(amount, from_currency, to_currency)
        
        # Display the result
        if converted_amount is not None:
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
        else:
            print("Invalid currency conversion.")
        
        # Ask if the user wants to perform another conversion
        another_conversion = input("Do you want to perform another conversion? (y/n): ").lower()
        
        # Exit the program if the user types 'n'
        if another_conversion == 'n':
            print("Thank you for using the Currency Converter!")
            break
        # Continue the loop if the user types 'y' (no message displayed)
        elif another_conversion == 'y':
            continue
        # Handle invalid input
        else:
            print("Invalid input. Please type 'y' or 'n'.")

# Run the program
if __name__ == "__main__":
    main()