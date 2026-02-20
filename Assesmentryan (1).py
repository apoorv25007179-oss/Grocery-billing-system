def calculate_bill():
    try:
    
        item1 = float(input("Enter the price of the first item: $"))
        item2 = float(input("Enter the price of the second item: $"))
        item3 = float(input("Enter the price of the third item: $"))

        
        total_cost = item1 + item2 + item3

        discount = 0.0

        
        if total_cost > 50.00:
            discount = total_cost * 0.10
            
        
        final_amount = total_cost - discount

        
        print("\n--- Customer Receipt ---")
        print(f"Original Total: ${total_cost:.2f}")
        
        
        if discount > 0:
            print(f"Discount (10%): ${discount:.2f}")
            
        print(f"Final Amount:   ${final_amount:.2f}")
        print("------------------------")

    except ValueError:
        print("Invalid input. Please enter valid numerical prices.")

if __name__ == "__main__":
    calculate_bill()
