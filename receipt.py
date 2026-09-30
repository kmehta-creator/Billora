from billing import create_bill
from customer import customer_details
from product import all_products
from shop import view_shop

def print_receipt(bill,shop):
    print("\n^^^^^***^^^^^***^^^^^***^^^^^***^^^^^***^^^^^")
    print("                  BILLORA")
    print("             'SMART SHOP BILLING'")
    print("_____---_____---_____---_____---_____---_____")

    print("\nShop Name     :", shop["name"])
    print("Shop Address  :", shop["address"])
    print("License Number:", shop["license"])

    print("\nCustomer Name :", bill["Customer"]["CustomerName"])
    print("Mobile Number :", bill["Customer"]["MobileNumber"])

    print("\n_____________________________________________________________________")
    print(f"{'Product':<15}"
          f"{'Quantity':<13}"
          f"{'MRP/Pc':<17}"
          f"{'Discount':<14}"
          f"{'Cost'}")
    print("_____________________________________________________________________")

    for product in bill["Products"]:
        print(f"{product['ProductName']:<15}"
              f"{str(product['Quantity']) + ' pcs':<13}"
              f"{'Rs. ' + format(product['MRP per Piece'], '.2f'):<17}"
              f"{str(product['Discount% per Piece']) + '%':<14}"
              f"{'Rs. ' + format(product['Total Price'], '.2f')}")

    print("---------------------------------------------------------------------")
    print("Grand Total :", "Rs.", format(bill["Grand Total"], ".2f"))
    print("Total Saved :", "Rs.", format(bill["Total Saved"], ".2f"))

if __name__ == "__main__":
    shop = view_shop()

    customer = customer_details()
    products = all_products()

    bill = create_bill(customer, products)

    print_receipt(bill,shop)
        