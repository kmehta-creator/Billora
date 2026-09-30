from shop import setup_shop, view_shop             #setup aur view ko main se connect kr rhe h
from customer import customer_details              #customer ke detail se connect kr rhe h
from product import all_products
from billing import create_bill
from receipt import print_receipt
from storage import save_bill, load_bills

def shop_menu():
       print("\n      SHOP SETUP & INFORMATION      ")       #heading dikhaya
       print("1: Set Up Your Shop")                          #yeh 3 options
       print("2: View Your Shop Information")
       print("3: Back to Main Menu")   

       shop_choice = int(input("ENTER YOUR CHOICE(1-3): "))

       if shop_choice==1:         #1st me shop setup          
            setup_shop()

       elif shop_choice==2:     #2nd me shop info. view
            shop=view_shop()

            print("\n          SHOP INFORMATION            ")
            print("Shop Name     :", shop["name"])
            print("Shop Address  :", shop["address"])
            print("License Number:", shop["license"])
            print("---x---x---x---x---x---x---x---x---x---x---")

       elif shop_choice==3:     #3rd me wapas main menu
            return

       else:
            print("\nInvalid choice. Please try again.")         #ant-shant me invalid

       
def show_main_menu():                              #display of main menu
    
    print("\n~~~**~~~**~~~**~~~**~~~**~~~**~~~**~~~**~~~")    #upper border(mero design)
    print("                BILLORA")                          #Title display
    print("        Smart Shop Billing System")              #slogan display
    print("***~~***~~***~~***~~***~~***~~***~~***~~***")      #lower border(mahro design)
    print("1: Create New Bill")              #1st option- Creating a new bill
    print("2: View Bill History")            #2nd option- viewing bill history(if any)
    print("3: Shop setup and Information")   #3rd option- Viewing shop info. (if already made) or Setting up new shop info.
    print("4: Exit")                         #4th option- exiting Billora   


def main():         # defining main function. je prog. control krto h.
    while True:
        show_main_menu()    #running main menu

        choice=int(input("ENTER YOUR CHOICE(1-4): "))               #taking input of choice

        if choice==1:
            print("\n'Create New Bill' selected.")               #display of 1st option

            shop=view_shop()
            customer=customer_details()                          #detail batai ke save kr lao
            products = all_products()

            bill = create_bill(customer, products)
            save_bill(bill)
            print_receipt(bill, shop)

        elif choice==2:
            print("\n'Bill History' selected.")                  #display of 2nd option

            bills = load_bills()

            for bill in bills:
                print("\nCustomer Name :", bill["Customer"]["CustomerName"])
                print("Mobile Number :", bill["Customer"]["MobileNumber"])
                print("Grand Total   : Rs.", format(bill["Grand Total"], ".2f"))
                print("Total Saved   : Rs.", format(bill["Total Saved"], ".2f"))
                print("----------------------------------------")

        elif choice==3:
            print("\n'Shop setup and Information' selected.")     #display of 3rd option
            shop_menu()
        
        elif choice==4:
            print("\n'Exit' selected.")                          #display of 4th option
            print("\nTHANK YOU for using BILLORA!")              #exit message
            break

        else:
            print("\nInvalid choice. Please try again.")        #If invalid choice is opted


if __name__=="__main__":             #yeh python ka special variable h. isse python confuse nhi hoga.
    main()                                 # ye main() ko run karaega.
