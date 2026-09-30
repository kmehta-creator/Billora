from validation import valid_name, valid_mobile

def customer_details():                         #customer ki detail ka fun. def.
    print("\n  !-- CUSTOMER DETAILS --!  ")                #uppar ka title

    customer_name = input("Enter customer name: ")       #naam bharna

    while not valid_name(customer_name):
        print("Invalid name. Please enter a name.")
        customer_name = input("Enter customer name: ")

    customer_mobile = input("Enter customer mobile: ")   #mob. no. bharna

    while not valid_mobile(customer_mobile):
        print("Invalid mobile number. Please enter a 10-digit number.")
        customer_mobile = input("Enter customer mobile: ")

    customer_details = {                            #details ek jagah rakh dao
        "CustomerName": customer_name,
        "MobileNumber": customer_mobile
    }

    return customer_details                         #details kou billora bheja


if __name__=="__main__":
    details=customer_details()
    print("\n CUSTOMER DETAILS entered successfully.")     #confirm statement.
    print(details)