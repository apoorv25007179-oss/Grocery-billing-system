item1 = float(input("Enter price of Item 1:$"))
item2 = float(input("Enter price of Item 2:$"))
item3 = float(input("Enter price of Item 3:$"))
total = item1 + item2 + item3

discount = 0

if total > 50:
    discount = total * 0.10
final_amount = total - discount

print("\n----- Billing Summary -----")
print("Original Total: $", round(total, 2))
print("Discount: $", round(discount, 2))
print("Final Payable Amount: $", round(final_amount, 2))
print("Thankyou Visit Again")
