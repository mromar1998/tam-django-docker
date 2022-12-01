# python-django-tam

$ Things need to be considerd , all the CRUD method has been implmented for the Contact in the views.py even if it not been asked. SQLlite is used
in order to add more name and number you can access admin page 
user : omar
password : 123456

I saw it very simple and small schema so i went for the detail of all of them , 3 table , contact -> name , contact -> phonenumber.
It's a weak structure but I didnt spend much time on it.

![9d4d3937-eb01-429a-b75f-e05dec766222](https://user-images.githubusercontent.com/78378808/205107097-b494c736-2995-4b41-805e-758b84f14dbe.jpeg)

Going to the containerized using docker,
these step has been done by creating Dockerfile , after that creating .dockerignore to avoid copying the env files. 
To create Image I used the following command:
 # docker build -t python-django-tam . #
 
 after the image been created i went to run it using 
 
 # docker run -p 8000:8000 python-django-tam # without using -d #
 
 after this step i went to tag the image before pushing it

# docker tag python-django-tam mromar1998/python-django-tam #

# docker push mromar1998/python-django-tam #

and from here You can test the image

https://hub.docker.com/layers/mromar1998/python-django-tam/latest/images/sha256-c977f02e035fb27097b06ef3bd1903bbfb5d619923d24fcd7139e38ee0160a61?context=repo

thanks
  


