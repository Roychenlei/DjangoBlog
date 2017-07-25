# DjangoBlog

Step by step to a set a Django Blog:

1, Intall the pip, virtualenv

2, use the virtualenv and install the Django:
	$ virtualenv . 
	$ pip install django==1.11

3, init project ,set a superuser,migrate:
	$ django-admin.py create blog
	$ python manage.py createsuperuser
	

4, create apps in project:
	$ python manage.py startapp posts

...


