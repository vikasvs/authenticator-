# authenticator-


**Important**
Use Python3 and pip3 for everything
Download virtualenv - pip3 install virtualenv
cd into cloned directory
open up a virtual env - source env/bin/activate
run pip3 install -r requirements.txt to install all dependencies - MAKE SURE YOU DO THIS IN A VIRTUAL ENV
if you add a download save it to requirements.txt with pip freeze > requirements. txt.

dont commit from virtual env - run "deactivate" to deactivate it then push


**Stuff that needs to get done**
*Infrasturcture*
- design employer side of the application
- craft email/link structure for employer to send 


*backend*
- Verify offer letter - need some method of externally checking the offer letter on our end
- send email to the employer getting verification and posting on feed
- make publicly shareable link to profile
- Need method of adding more than 1 offer letter, should be able to add previous offer letters
- do we need to validate employers emails
- if employer gets laid off what do we do with email


**Django stuff**

To run code cd into authenticate_project and run python3 manage.py runserver. If yu go to localhost:8000 you should see the home page.

**Whats in the code/where is stuff**

Django works in seperate folders essentially. The authenticate_project folder within the authenticate_project folder is where high level stuff is that ties everything togeter. the authenticate folder is where all the work is realy happening though. urls.py is where we link and attach pages. views.py is where you write backend code and render it through the frontend

Within templates, then authenticate is where the frontend happens. Here there are 3 pages, base, about, and home. every page should be a subset of base, do the bulk of the work there that can be aggregated and do unique work in the other tabs. If you want to add backend play around with views.py, if you want to add frontend play around with the templates


**tutorials**
https://www.youtube.com/watch?v=a48xeeo5Vnk
https://www.youtube.com/watch?v=UmljXZIypDc
https://www.youtube.com/watch?v=qDwdMDQ8oX4&t=124s
https://www.youtube.com/watch?v=609pxEMfung&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=15
