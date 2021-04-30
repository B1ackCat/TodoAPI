# TodoAPI
Simple TodoAPI H1

How to use:
1.pip install -r requirements.txt  
2.Create Mysql DB "todo_app" (Change Settings.py DataBase setting)  
3.python manage.py makemigrations  
4.python manage.py migrate  
5.python mange.py runserver  

URL LIST  
/todos/ : Show Todo_list  
/comment/ : Show comment  
/todos/{id} : show todo<id> detail  
/comment/{id} : show comment<id> detail  
