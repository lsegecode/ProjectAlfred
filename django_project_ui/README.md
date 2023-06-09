Prerequisites:
- Python should be installed
- pip installation
- Install virtual environment
Step 1 : Create a new virtual environment
- Create a virtual environment with the command:
mkvirtualenv name_of_environment (linux)
- Activate virtual environment with the command:
workon name_of_environment (linux)
Step 2: Django
- Install django:
sudo pip3 install Django (linux)

Step 3: Create project
- Create project’s folder and access it
- Create a Django project
django-admin startproject name_of_project

*** FROM HERE TO CREATE NEW ui SECTIONS ***

Step 4: Create section (application)
- Create new application:
python3 manage.py startapp name_of_application

Step 5: Settings
- Review settings.py file to:
- Specify/check database and other configurations
- Register new application on the project
INSTALLED_APPS = [
'name_of_application.apps.NameOfApplicationConfig',
]

Step 6: URLs mapping
- Go to name_of_project/urls.py and register new application

urlpatterns += [
path('name_of_application/', include('name_of_application.urls')),
]
- Go to name_of_project/name_of_application/ and create urls.py, to map the application internals:
from django.conf.urls import path
from . import views

urlpatterns = [
]

Step 7: Create templates
- In name_of_aplication/templates add your template files (e.g. view_name.html)

Step 8: Register templates
- In name_of_aplication/views.py create templates path and add new template views
TEMPLATE_DIRS = (
'os.path.join(BASE_DIR, “templates”),'
def view_name(request):
return render(request, 'view_name.html')
- In name_of_aplication/urls.py
urlpatterns = [path('',views.view_name, name = 'view_name')
]

Step 9: Execute migrations
On terminal:
- python3 manage.py makemigrations
- python3 manage.py migrate

Step 10: Run server
- python3 manage.py runserver

Step 11: Run server
-Get access on http://127.0.0.1:8000/ (default)

For more information you can refer to the documents in spanish:
- Django and UI implementation (summary)  https://docs.google.com/document/d/1ffxxQUuS2WFVXM4oqTeH_Sg-JKHhrY5t/edit?usp=sharing&ouid=107518907780966616100&rtpof=true&sd=true
- Complete description https://docs.google.com/document/d/1Yi9pclo0uemuqJjr6VKR8zlA_eB6gQsT/edit?usp=sharing&ouid=107518907780966616100&rtpof=true&sd=true
