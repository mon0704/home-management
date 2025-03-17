# Home Rental & Property Management API

## Project Overview

The Home Rental & Property Management API is a web-based system designed to help landlords and tenants manage rental properties efficiently. It provides features for listing properties, managing leases, processing rent payments, and handling maintenance requests. This API enables property managers to streamline their operations while giving tenants a convenient way to track rental-related activities.

## Table of Contents

- [Real-World Relevance](#real-world-relevance)
- [API Endpoints](#api-endpoints)
  - [Property Management](#property-management)
  - [Lease Management](#lease-management)
  - [Payment Processing](#payment-processing)
  - [Maintenance Requests](#maintenance-requests)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Testing the API](#testing-the-api)
- [Contributing](#contributing)
- [License](#license)

## Real-World Relevance

This API addresses common challenges in rental management, such as:
- Keeping track of property listings and availability.
- Managing lease agreements and renewals.
- Handling rent payments and tracking overdue balances.
- Facilitating maintenance request submissions and tracking their resolution.

By digitizing these processes, landlords and tenants experience improved efficiency and transparency.

## API Endpoints

### Property Management
- **GET** `/api/properties/` - Retrieve a list of all rental properties.
- **GET** `/api/properties/{id}/` - Retrieve details of a specific property.
- **POST** `/api/properties/` - Add a new property listing.
- **PUT** `/api/properties/{id}/` - Update property details.
- **DELETE** `/api/properties/{id}/` - Remove a property listing.

### Lease Management
- **GET** `/api/leases/` - Retrieve all active lease agreements.
- **GET** `/api/leases/{id}/` - Retrieve details of a specific lease.
- **POST** `/api/leases/` - Create a new lease agreement.
- **PUT** `/api/leases/{id}/` - Update lease terms.
- **DELETE** `/api/leases/{id}/` - Terminate a lease.

### Payment Processing
- **GET** `/api/payments/` - Retrieve all payments.
- **GET** `/api/payments/{id}/` - Retrieve details of a specific payment.
- **POST** `/api/payments/` - Record a new rent payment.
- **PUT** `/api/payments/{id}/` - Update payment status.
- **DELETE** `/api/payments/{id}/` - Remove a payment record.

### Maintenance Requests
- **GET** `/api/maintenance/` - Retrieve all maintenance requests.
- **GET** `/api/maintenance/{id}/` - Retrieve details of a specific maintenance request.
- **POST** `/api/maintenance/` - Submit a new maintenance request.
- **PUT** `/api/maintenance/{id}/` - Update the status of a maintenance request.
- **DELETE** `/api/maintenance/{id}/` - Remove a maintenance request.

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL (or SQLite for development)
- Postman (for testing)

