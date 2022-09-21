 Data2bot-api-testHi,
this is just a simple api.

To run it locally,
1 clone ripo
2 create virtual environment
3 cd to project directory install requirement.txt file 
4 run python manage.py runserver.

routs:
http://127.0.0.1:8000/redoc/  for reading api documentation
http://127.0.0.1:8000/swagger/  for documentation also
http://127.0.0.1:8000/admin/  for admin (super user details, username magnus, password root)
http://127.0.0.1:8000/api/customers/ for registration and customer list(GET/POST Request)
http://127.0.0.1:8000/api/token/   for login token request.
http://127.0.0.1:8000/api/token/refresh
