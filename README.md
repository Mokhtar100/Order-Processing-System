# Order Processing System Documentation

## Introduction
The Order Processing System is a Django-based application designed to simplify the order processing for an online store. It allows users to browse products, add them to the cart, and complete the checkout process with confirmation emails to customers.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python (version 3.x)
- Django (version 3.x)
- sqlite3

1. Clone the repository:
   ```bash
   git clone https://github.com/Mokhtar100/Order-Processing-System.git
2. Navigate to the project directory:
   ```bash
   cd Order-Processing-System
3. Install Django:
   ```bash
   pip install django
4. Run the server:
   ```bash
   python manage.py runserver
## Usage
### Creating Products:
1. Log in to the Django admin panel (/admin).:
   ```bash
   Username: mokh
   Password: mokh
2. Go to the Products section in admin panel and Add Products.
3. Fill in the required details and save.

### Buy Products:
1. Log in to (/) to see all products.
2. Add products to cart .

### Managing Cart:
1. Log in to (/cart) to see products in your cart.
2. Total amount and The quantity of each product you purchased.
3. To complete the purchase process press ("Pay Now") to go checkout.

### Checkout Process:
1. Log in to (/checkout) or when press ("Pay Now") in (/cart) automatically go to checkout.
2. Add your name.
3. Add your email to send a confirmation email have the order ID, purchased items, and total amount.
4. press ("Submit") to finish your progress.

## Testing:
- You can test the Order Processing System by navigating to the following URLs:
   ```bash
   Products: http://localhost:8000/
   Admin Panel: http://localhost:8000/admin/
   Cart: http://localhost:8000/cart/
   Checkout: http://localhost:8000/checkout/
