def valid_quantity(quantity):
    return quantity > 0

def valid_mrp(mrp):
    return mrp >= 0

def valid_discount(discount):
    return 0 <= discount <= 100

def valid_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10

def valid_name(name):
    return name.strip() != ""