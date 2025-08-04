# "Grocery Billing System"

# items = {
#     "apple": 30 ,
#     "banana": 40 ,
#     "grapes": 70 , 
#     "milk" : 20 ,
#     "bread": 65
    
# }
# cart = []
# # cart = ["apple","banana","bread", "grapes", "apple"]
# total = 0

# for i in cart:
    
#     total += items[i]
# print("items bought : ", cart)
# print("Total bill :", total)



print("-----------Grocery Billing System------------")


items = {
    "apple": 100 ,
    "banana": 60 ,
    "grapes": 70 , 
    "milk" : 25 ,
    "bread": 30
    
    
}
cart = []
print("Avalible items:")
for item, price in items.items():
    print(f"- {item.title()}: ₹{price}")
    
print("Type the items you want to buy (type 'enough' to finish):")
    
    
while True:
    product = input("Enter the items:").lower()
    if product == "enough":
        break
    if product in items:
        cart.append(product)
    else:
        print("Item not available. Please choose from the list.")
            
total = 0
for item in cart:
    total += items[item]
print("\n🛒 Items Bought:", cart)
print("💰 Total Bill: ₹", total)

print("----------Thank you for visiting our S-Mart-------")