print("Python Profit Calculator")
money=float(input('Enter the amount of money:'))
start_price=float(input('Enter the price bought:'))
end_price=float(input('Enter the price sold:'))
profit=(money/start_price)*end_price-money
print('%0.3f is the output profit.' %(profit))
