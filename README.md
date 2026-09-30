# Billora — Smart Shop Billing System

Billora is a Python-based billing system that I built to make the basic billing process of a shop simple and organized.

It allows the shopkeeper to save shop details, enter customer and product details, calculate discounts and final prices, generate a proper bill receipt, and keep a history of previous bills.

The project is made using separate Python files for different tasks, and JSON files are used to store the shop and billing data.

## Features

- Shop setup and shop information management
- Customer details entry
- Product and quantity entry
- Discount and billing calculations
- Automatic calculation of total amount and savings
- Proper bill receipt generation
- Bill history storage and viewing
- Input validation for important details
- JSON-based data storage

## Technologies Used

- Python
- JSON
- Visual Studio Code
- Git and GitHub

## How to Run

1. Open the Billora project folder in Visual Studio Code.
2. Open the terminal in the project folder.
3. Run the following command:

```text
python main.py```

4. The Billora main menu will appear in the terminal.
5. Choose the required option and follow the instructions shown by the program.

## Project Structure

```text
Billora/
├── main.py
├── shop.py
├── customer.py
├── product.py
├── calculation.py
├── billing.py
├── receipt.py
├── validation.py
├── storage.py
├── test_billora.py
├── data/
│   ├── shop.json
│   └── bills.json
├── README.md
└── statement.md

## Testing

The project includes a separate test file named `test_billora.py`.

The calculation functions were tested for:

- Discount calculation
- Final price calculation
- Total price calculation
- Total savings calculation

All four tests passed successfully.

## Author

Developed by Kirti Mehta as a Python project for learning and applying programming concepts through a practical billing system.