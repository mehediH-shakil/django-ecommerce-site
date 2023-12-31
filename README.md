# Django E-commerce Site

This project is an E-commerce website built using Django, which incorporates user authentication, a shopping cart, purchase and payment integration, an admin interface, and a RESTful API.

## Project Setup

To run the project, follow these steps:

1. Clone the project repository:

```
https://github.com/mehediH-shakil/django-ecommerce-site.git
```

2. Navigate to the project directory:

```
cd django-ecommerce-site
```

3. Create and activate a virtual environment:

```
python -m venv env
source env/bin/activate (for Linux/Mac) or env\Scripts\activate (for Windows)
```

4. Install the project dependencies:

```
pip install -r requirements.txt
```

5. Apply the database migrations:

```
python manage.py migrate
```

6. Start the development server:

```
python manage.py runserver
```

7. Open your web browser and access the website at `http://localhost:8000`.

## User Authentication

The user authentication functionality includes user registration, login, and logout. Users can also update their profile details.

## Product Management

The project includes a database of products with fields such as name, description, price, image, and stock status. All products are displayed on a paginated view.

## Shopping Cart

Users can add products to their shopping cart and remove them as needed. The shopping cart updates dynamically as items are added or removed. The stock status of products is also updated accordingly.

## Purchases and Payment Integration

The checkout process allows users to enter shipping information and payment details. The project integrates with a real payment gateway (e.g., Stripe, PayPal) to handle payments. After a successful transaction, a purchase receipt (order summary) is generated.

## Admin Interface

The project includes an admin interface built using Django's built-in capabilities. The admin has the ability to add, edit, and delete products.

## RESTful API

The project implements a RESTful API using Django REST Framework. The API provides endpoints to retrieve product information and place orders. All endpoints require appropriate authentication and permissions.

## User Reviews

Logged-in users can review products they have purchased. These reviews are displayed on the respective product pages.

## Report

A brief report is included, which explains any challenges encountered during development and how they were addressed.

## Notes
- The project utilizes the `Pillow` library for image processing. Ensure that you have the required dependencies installed on your system.

Please refer to the provided report for further details on the challenges faced and their resolutions.

For any questions or support, please contact mehedi.vu.cse@gmail.com.
