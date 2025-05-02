def calculate_tariff(trade_deficit, total_imports):
    #Calculate the deficit ratio as a percentage
    ratio = (trade_deficit / total_imports) * 100
    # Enforce a minimum tariff of 10%
    return max(10, ratio)

# Example usage
tariff = calculate_tariff(20e9, 100e9)  # $20B deficit on $100B imports yields a 20% tariff
print(f"The tariff rate should be {tariff}%")