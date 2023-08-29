from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("Enter the amount: "))

a_currency = input("From Currency: ").upper()

b_currency = input("To Currency: ").upper()

print(a_currency, " To ", b_currency, amount)

result = c.convert(a_currency, b_currency, amount)

print(result)
