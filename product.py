from validation import valid_quantity, valid_mrp, valid_discount

def product_details():                    #product details kao func.
    
    print("\nPRODUCT DETAILS :~ ")            #upar ke line

    product_name = input("Enter product name: ")    #product naam lao
    quantity = int(input("Enter quantity: "))       #kitne lao
    while not valid_quantity(quantity):
        print("Invalid quantity. Please enter a quantity greater than 0.")
        quantity = int(input("Enter quantity: "))

    mrp = float(input("Enter MRP/Product: "))       #MRP kitni h 1 pec ki
    while not valid_mrp(mrp):
        print("Invalid MRP. Please enter a non-negative value.")
        mrp = float(input("Enter MRP/Product: "))

    discount = float(input("Enter discount/product (%): ")) #discount kitno h(%)
    while not valid_discount(discount):
        print("Invalid discount. Please enter a value between 0 and 100.")
        discount = float(input("Enter discount/product (%): "))
        
    product_details = {
        "ProductName": product_name,
        "Quantity": quantity,
        "MRP per Piece": mrp,
        "Discount% per Piece": discount
    }

    return product_details                      #product ke details Billora ko bhejo


def all_products():                         #saare products lene ka func.
    products = []                               #products ko store karn kilist
    
    while True:
        product = product_details()            #product details lao
        products.append(product)               #product ke list jodo
    
        more = input("Do you want to add another product? (yes/no): ")
    
        if more.lower() != "yes":
            break
    
    return products                              #products ko bhejo        

if __name__ == "__main__":
    details =all_products()                          #sare products ki detail dalao
    print("\nPRODUCT DETAILS entered successfully.")     #confirm statement h
    print(details)                                       #details print kar di                  
        