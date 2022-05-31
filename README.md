# Hel
HEL - Application de mise en relation de professionnel. Platform of setting in relation of professional.

Écrite en python et sur le framework Django, cette application permet à une entité de mettre en relation des professionnels
qu'elle a dans sa base de données et des clients qui s'authentifieront sur la plateforme et créeront des demandes pour certaines catégories. 

Written in python and on the Django framework, this application allows an entity to connect professionals it has in its database 
with customers who will authenticate on the platform and create requests for certain categories.


----------------------------------------------- To run the app on your laptop -----------------------------------------------

Configuration for Windows using command lines:
- Install|Update Python on your device : https://www.python.org/downloads/
- Go to repository : cd ../pmr
- Create a virtual environment : python -m venv [Name]
- Install Django and all dependencies : pip install requirements
- Populate database : python manage.py makemigrations
                     python manage.py migrate
- Start app : python manage.py runserver
- Open your browser and go to http://127.0.0.1:8000/
