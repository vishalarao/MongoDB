MongoDB
================
	operations to add,update and delete records in DB

Installation
-----------------------
Run below command in command prompt
	pip install Flask-MongoAlchemy==0.7.2,Flask==1.1.0

Running
-------------------------
Run below command

	python mongo.py

Note : Before running make sure the MongoDB is running @ localhost:27017

Exapmle 1: Adding Employee
-------------------------

	C:\mongodb>python mongo.py
	Enter your choice :
	1 : Add Employee
	2 : Update Employee
	3 : Delete Employee:
	4 : To display all employees
	1
	Enter the Employee name to add : Testing
	Employee not found
	Please enter Employee email to add to DB : Testing@testing.com
	Employee Testing Added
	
Example 2:Modifying if the user exsists
-----------------------------

	C:\mongodb>python mongo.py
	Enter your choice :
	1 : Add Employee
	2 : Update Employee
	3 : Delete Employee:
	4 : To display all employees
	1
	Enter the Employee name to add : Testing
	Employee name already exsists, Do you want to modify it? y/n : y
	Employee name: Testing , Email :  Testing@testing.com
	Enter the name to modify : Testing
	Enter the Email to modify : Testing@test.com
	Employee Testing modified

Exapmle 3: Updating a Employee
--------------------------------

	C:\mongodb>python mongo.py
	Enter your choice :
	1 : Add Employee
	2 : Update Employee
	3 : Delete Employee:
	4 : To display all employees
	2
	Enter the Employee name to update : Testing
	Do you want to modify it? y/n : y
	Employee name: Testing , Email : Testing@test.com
	Enter the Email to modify : Testing@testing.com
	Employee Testing modified

Example 4 : Display all Employees
-----------------------------------------
	C:\Users\vishal.a.rao\Desktop\groovy>python mongo.py
	Enter your choice :
	1 : Add Employee
	2 : Update Employee
	3 : Delete Employee:
	4 : To display all employees
	4
	[{'name': u'Testing', 'email': u'Testing@test.com'}]	

Example 5: Deleting a Employee
-----------------------------------

	C:\mongodb>python mongo.py
	Enter your choice :
	1 : Add Employee
	2 : Update Employee
	3 : Delete Employee:
	4 : To display all employees
	3
	Enter the Employee name to delete : Testing
	Employee Testing removed was removed