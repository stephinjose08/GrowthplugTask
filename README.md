# Ebook CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.
-
#### Requirements
* Django==4.1.2
* django-filter==22.1
* djangorestframework==3.14.0
* djangorestframework-simplejwt==5.2.2

#### Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

_python -m venv env_

After this, it is necessary to activate the virtual environment You can install all the required dependencies by running

_pip install -r requirements.txt_
# Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources.


### Ebook
In our case, we have one  resource, book for list and retrive  books  and ebookrud/<pk> for update and destroy books, so we will use the following URLS - /book/  ,/book/<pk>and /ebookrud/<pk> for collections ,elements,update,destroy respectively:
  
/bookactions/ used for filter,search,ordering in ebook 
  
### Genre 
  
  In our case, we have one  resource, genre for list and retrive  genre  and genrerud/<pk> for update and destroy genre, so we will use the following URLS - /genre/  ,/genre/<pk>and /ebookrud/<pk> for collections ,elements,update,destroy respectively:
  
/genreactions/ used for filter,search,ordering in genre 
 
  ### User
  
   In our case, we have one  resource, login for user login and register for new user registration  userlist   for list the users, so we will use the following URLS - /login/  ,/register/, /userlist/ for collections ,foro login,register new user,get user list  respectively:
  
  
  
  
  [All the test cases using PostMan](https://documenter.getpostman.com/view/21786458/2s8YmPtMnU)
