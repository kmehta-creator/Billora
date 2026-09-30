def cal_discount(mrp, discount):       #discount amnt. define kiya
    discount_amnt = mrp * (discount/100)  #discount calculate kiya
    return discount_amnt                   #discount amount bhejao

def final_price(mrp, discount):                      #final price nikalno h
    discount_amnt = cal_discount(mrp, discount)      
    price = mrp - discount_amnt                      #pricing karao
    return price                                     #price niakalao

def total_price(mrp, discount, quantity):        #total price ko func.
    price = final_price(mrp, discount)           #discounted price h
    total = price * quantity                     #quantity ke hisab se total price
    return total                                 #total price bhejao

def total_savings(mrp, discount, quantity):        #total amount ko func.
    discount_amnt = cal_discount(mrp, discount)    #discount/pec h
    savings = discount_amnt * quantity             #bachat
    return savings                                 #saving bhejao

def calculate_product(product):                         #ek product ka calculation
    mrp = product["MRP per Piece"]
    discount = product["Discount% per Piece"]
    quantity = product["Quantity"]

    discount_amnt = cal_discount(mrp, discount)
    price = final_price(mrp, discount)
    total = total_price(mrp, discount, quantity)
    savings = total_savings(mrp, discount, quantity)

    calculated_product = {
        "ProductName": product["ProductName"],
        "Quantity": quantity,
        "MRP per Piece": mrp,
        "Discount% per Piece": discount,
        "Discount Amount per Piece": discount_amnt,
        "Price per Piece": price,
        "Total Price": total,
        "Total Savings": savings
    }

    return calculated_product

def calculate_all_products(products):             #saare products ka calculation
    calculated_products = []                      #calculated products ki list

    for product in products:
        calculated = calculate_product(product)   #ek product calculate karo
        calculated_products.append(calculated)    #calculated product list me jodo

    return calculated_products                     #saare calculated products bhejo

def calculate_bill_totals(calculated_products):       #poore bill ka total
    grand_total = 0                                  #total ki starting value
    total_saved = 0                                  #saving ki starting value

    for product in calculated_products:
        grand_total += product["Total Price"]        #har product ka total jodo
        total_saved += product["Total Savings"]      #har product ki saving jodo

    return grand_total, total_saved                  #dono totals bhejo

if __name__ == "__main__":
    products = [
        {
            "ProductName": "Soap",
            "Quantity": 3,
            "MRP per Piece": 30.0,
            "Discount% per Piece": 10.0
        },
        {
            "ProductName": "Juice",
            "Quantity": 2,
            "MRP per Piece": 10.0,
            "Discount% per Piece": 10.0
        }
    ]

    calculated_products = calculate_all_products(products)
    print(calculated_products)

    grand_total, total_saved = calculate_bill_totals(calculated_products)

    print("Grand Total:", grand_total)
    print("Total Saved:", total_saved)