# Restaurant-Kitchen-Service


1. Project Overview
2. Features
3. Technologies Used
4. Project Installation
5. Project Setup
   - Create a Virtual Environment
   - Install Dependencies
6. Start the Project
7. Create the Application
8. Database Setup
9. Running the Development Server
10. Important Note
11. Testing the Application
12. Conclusion

## Project Overview
The Restaurant Kitchen Service is a Django web application designed to manage a restaurant's kitchen operations. It allows cooks to create new dishes and dish types and to assign responsibilities for each dish. The application features a user-friendly interface for managing dishes, cooks, and dish types.

## Features
- User Authentication: Secure login for cooks and admin users.
- Dish Management: Manage categories for dishes.
- Dish Type Management: Manage categories for dishes.
- Cook Management: Manage cooks and their details, including experience.
- Responsive Web Interface: Intuitive design for easy navigation and use.

## Technologies Used
- Django 5.0.7
- Python 3.12.2
- SQLite
- HTML/CSS for front-end design 

You can see these files in `requirements.txt`.

## Project Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Restaurant-Kitchen-Service.git
   cd Restaurant-Kitchen-Service
```
   
## Project Setup 
1. Create a virtual environment, activate it and install Django via pip:
```bash
python -m venv venv
source .venv/bin/activate
# On Windows use:
.venv\Scripts\activate
pip install django
```
## Install Dependencies
Make sure to run requirements.txt
```bash 
pip install -r requirements.txt 
```

## Start the Project
To start the Django project, run the following command in the terminal:
```bash 
django-admin startproject RestaurantKitchenService .
```

## Create the Application
Next, create the "kitchen" app within your project:
```bash 
python manage.py startapp kitchen
```

## Database Setup
Before running the application, make sure to run migrations to set up the database:
```bash 
python manage.py makemigrations
python manage.py migrate
```

## Running the Development Server
You can run the development server with the following command:
```bash 
python manage.py runserver
```

Visit "http://127.0.0.1:8000/" in your web browser to access the application.

## Important Note
Please note that all main functionalities, such as managing dishes, cooks and dish types, are performed through the web interface of the application. It is recommended to use the website for all operations related to dish management and cook assignments.


## Testing the Application
To run tests for the application, use the following command:
```bash 
python manage.py test kitchen.tests
```

## Conclusion
You are now ready to use the Restaurant Kitchen Service application.