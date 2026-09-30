from calculation import (
    cal_discount,
    final_price,
    total_price,
    total_savings
)

discount = cal_discount(100, 20)

assert discount == 20

print("Discount calculation test passed.")

price = final_price(100, 20)

assert price == 80

print("Final price calculation test passed.")

total = total_price(100, 20, 3)

assert total == 240

print("Total price calculation test passed.")

savings = total_savings(100, 20, 3)

assert savings == 60

print("Total savings calculation test passed.")