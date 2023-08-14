bill_amount = 47.28
tip_percentage = 15
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount
each_share = total_amount / 2

# Output the results
print("Tip amount: $",tip_amount)
print("Total amount to pay: $",total_amount)
print("Each person needs to pay: $",each_share)
