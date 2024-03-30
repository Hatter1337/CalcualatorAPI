# Calculator API

## Overview

This project implements a web-based calculator application that performs basic arithmetic operations:
(+) addition, (-) subtraction, (*) multiplication, and (/) division. The architecture separates the business logic from the presentation layer and ensures that the system is extendable for future enhancements.

The application adheres to OOP principles and is designed with future extensions in mind.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

- Docker
- Docker Compose

### Installing

1. Clone the repository:
`$ git clone git@github.com:Hatter1337/CalcualatorAPI.git`
2. Navigate to the project directory:
`$ cd CalculatorAPI`
3. Build and run the Docker containers:
`$ docker-compose up --build`

#### The web-based calculator can be accessed at http://localhost.

#### The REST API is accessible at http://127.0.0.1:8000.
Swagger: http://127.0.0.1:8000/docs.