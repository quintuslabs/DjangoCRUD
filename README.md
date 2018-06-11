# DjangoCRUD
This ia a Simple CRUD Operation in Django with MYSQL Database

1.Clone this Project<br/>
2.Create employee Database in Mysql<br/>
3. Move to your Project Folder<br/>
4. Activate VirtualEnvironment<br/>
5. Change settings.py<br/>
<br/>
<br/>
<pre>
DATABASES = {<br/>
   'default': {<br/>
   'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employees',
        'USER': 'root',  
        'PASSWORD': '',
        'HOST': '127.0.0.1',//localhost  
        'PORT': '',     
    }
}</pre>
<br/>
<br/>
6.Run Command "python manage.py makemigrations" in Command Prompt<br/>
7.Run Command "python manage.py migrate" in Command Prompot<br/>
8. After Successfull migration Run Server "python manage.py runserver"<br/>
9.open Link http://127.0.0.1:8000/ <br/>
