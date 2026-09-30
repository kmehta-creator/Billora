import json                    #using python storage

shop_file="data/shop.json"         #file ka location de di

def setup_shop():                       #defining shop function
    print("\n|| SHOP SETUP ||")         #title printing

    shop_name = input("Enter your shop name: ")                   #Shop ka naam
    shop_address = input("Enter your shop address: ")              #Shop ka address
    shop_license = input("Enter your shop's license number: ")    #shop ka lic. no.

    shop_details = {                    #teeno info. sath me...
        "name": shop_name,
        "address": shop_address,
        "license": shop_license
    }

    with open(shop_file, "w") as file:               #w-write mode : python me file likhna h
        json.dump(shop_details, file, indent=4)      #json.dump() : dic. ko json me convert krke store krna   

    return shop_details               #info. back to billora

def view_shop():
    with open(shop_file, "r") as file:
        shop_details = json.load(file)

    return shop_details

if __name__ == "__main__":            #python ka function h
   view_shop()