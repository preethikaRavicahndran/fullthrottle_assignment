#Populated database using custom commands like

# For creating users
python manage.py creating_user 'Glinda Southgood' Asia/Kolkata  

# For creating multiple activity periods for Particular user
python manage.py create_user_activity_periods c4a14e5104484e3bb0e02a4f218a85d2 'Jan 2 2020  2:34PM' 'Feb 5 2020 6:54PM' 


# Admin credentials
username: preethika
password: test

#Get User Details API
URL: http://127.0.0.1:8000/fullthrottle/user_details
Basic Auth: username: preethika
            password: test        # Only admin can get user details
            


#Commands used for Migrations
python manage.py makemigrations
python manage.py migrate

#commands used to runserver
python manage.py runserver
            
            
   