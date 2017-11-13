Assumptions/Requirements:

Django Version: 1.10.6
Python Version: 2.7.5

Steps:
1. python manage.py createsuperuser  <Enter Credentials as per choice>
2. python manage.py runserver
3. Open URL: localhost:8000/login/ 
4. Look for the instructions that follows.


Note:
1. The user should login to create forms.
2. All the answers fields should be marked with atleast one options.
3. After selecting input type for the answers, it can only be altered/updated by deleting the previous options/answers.
4. In the present scenario, only the current form that is created by the user is  displayed at the end. However, it is stored in the database. 
The code to give a choice to display the selected form is buggy and disabled in this. However, it can be read in the files.
5. The User must login again to create a new form. 
6 Please find the Screenshots file also with the project
