cost_price:= 200
selling_price:= 250

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No Profit, No Loss")
