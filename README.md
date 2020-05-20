# authenticator-


Django stuff

you need to install django, idk if installing it within the directory will make it work on your laptop if it doesnt run pip3 install django USE PYTHON3 AND PIP3 FOR EVERYTHING

once you have it you cd into authenticate_project and run python3 manage.py runserver. If yu go to localhost:8000 you should see the home page. There are currently two pages localhost:8000 and localhost:8000/about. 

Whats in the code/where is stuff

Django works in seperate folders essentially. The authenticate_project folder within the authenticate_project folder is where high level stuff is that ties everything togeter. the authenticate folder is where all the work is realy happening though. urls.py is where we link and attach pages. views.py is where you write backend code and render it through the frontend

Within templates, then authenticate is where the frontend happens. Here there are 3 pages, base, about, and home. every page should be a subset of base, do the bulk of the work there that can be aggregated and do unique work in the other tabs. If you want to add backend play around with views.py, if you want to add frontend play around with the templates


tutorials
https://www.youtube.com/watch?v=a48xeeo5Vnk
https://www.youtube.com/watch?v=UmljXZIypDc
https://www.youtube.com/watch?v=qDwdMDQ8oX4&t=124s
