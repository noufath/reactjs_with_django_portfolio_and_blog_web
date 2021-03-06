# Personal portfolio and web blog
Personal Web and Blog using Django as backend, Django Rest Framework and React.JS as frontend


## Dependencies
This web depends on :

    Database :
        - PostgreSQL 13.0

    Backend : 
        - Django 3.4.2
        - django-rest-framework 0.1.0
        - environ 1.0
        - Pillow 8.3.1
        - Psycopg2 2.9.1
        - Psycopg2-bin 2.9.1
    
    Frontend :
        - react ^17.0.2
        - @material-ui/core ^4.11.3
        - @material-ui/icons ^4.11.2
        - @mui/material ^5.0.2
        - @mui/icons-material ^5.0.3
        - axios ^0.22.0
        - typed.js ^2.0.11

## Environment file
Create an environment file in backend with the following parameters :

SECRET_KEY=YOUR_SECRET_KEY  
DJANGO_DEBUG=DJANGO_DEBUG_OPTION   
DATABASE_USER=YOUR_POSTGRES_USER   
DATABASE_PASS=YOUR_POSTGRESQL_PASSWORD   
DATABASE_NAME=YOUR_POSTGRESQL_DBNAME   
DATABASE_PORT=YOUR_POSTGRESQL_PORT   
DATABASE_HOST=YOUR_POSTGRESQL_HOST   
ALLOWED_HOSTS=localhost,127.0.0.1   
E_HOST=smtp.gmail.com   
E_PORT=587   
E_HOSTUSER=YOUR_EMAIL_SENDER_ACCOUNT   
E_HOSTPASSWORD=YOUR_EMAIL_SENDER_KEYAPP/ PASSWORD   
E_USETLS=True   


### [Live Preview](https://dc-portfolio-blog.herokuapp.com/)


### Home Page
![home page](https://user-images.githubusercontent.com/7325133/153144982-bf686e42-727c-460e-8b64-f3dcdbd3b015.png)


## Menubar
![menubar](https://user-images.githubusercontent.com/7325133/153145211-499205e0-f1e0-4d76-b221-947a052077c2.png)

## Portfolio page
Portfolio list fetch from Django Rest Framework
![portfolio](https://user-images.githubusercontent.com/7325133/153180211-dcbf76a9-0518-466a-a5ef-6ab2813b54e1.png)

## Contact Form Page
Every message that has been sent, backend server will send the message to the admin email.
![contact form](https://user-images.githubusercontent.com/7325133/153145912-5870d0da-4a99-4300-b138-4f873feefda1.png)

## Blog Page
Posts sent via the django admin page are displayed on the frontpage of the blog page.
![blogpage](https://user-images.githubusercontent.com/7325133/153146251-fe055c56-78e8-41bd-9e18-1ff6b1b31541.png)

## Detail post
![detail_post](https://user-images.githubusercontent.com/7325133/153153589-9bd31326-3df7-4281-abac-fd6d0267d5fb.png)

