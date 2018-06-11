# DjangoCRUD
This ia a Simple CRUD Operation in Django with MYSQL Database

1.Clone this Project
2.Create employee Database in Mysql
3. Move to your Project Folder
4. Activate VirtualEnvironment
5. Change settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employees',
        'USER': 'root',  
        'PASSWORD': '',
        'HOST': '127.0.0.1',//localhost  
        'PORT': '',     
    }
}

6.Run Command "python manage.py makemigrations" in Command Prompt
7.Run Command "python manage.py migrate" in Command Prompot
8. After Successfull migration Run Server "python manage.py runserver"
9.open Link http://127.0.0.1:8000/ 
