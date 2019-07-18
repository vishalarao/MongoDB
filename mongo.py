from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app=Flask(__name__)
 
app.config["MONGOALCHEMY_DATABASE"]="mydb"

db=MongoAlchemy(app)

class Emp_Collection(db.Document):
    name = db.StringField()
    email = db.StringField()

def get_emp(name):
    emp = Emp_Collection.query.filter(Emp_Collection.name==name).first()
    if emp:
        choice = raw_input('Employee name already exsists, Do you want to modify it? y/n : ')
        if choice in ('y','Y'):
            print 'Employee name: %s , Email : %s' % (emp.name,emp.email)
            emp.name = raw_input('Enter the name to modify : ')
            emp.email = raw_input('Enter the Email to modify : ')
            emp.save()
            print 'Employee %s modified' % (emp.name)
        elif choice in ('n','N'):
            print 'Employee name: %s , Email : %s' % (emp.name,emp.email)
        else:
            print 'Invalid choice'
    else:
        emp = Emp_Collection(name=name)
        print 'Employee not found'
        emp.email = raw_input('Please enter Employee email to add to DB :')
        emp.save()
        print 'Employee %s Added' % name
        
def get_emps():
    emps = Emp_Collection.query.filter().all()
    output=[]
    for emp in emps:
        data={}
        data['name']=emp.name
        data['email']=emp.email
        output.append(data)
    print output

def delete_emp(name):
    emp = Emp_Collection.query.filter(Emp_Collection.name==name).first()
    if emp:
        emp.remove()
        print 'Employee %s removed was removed' % name
    else:
        print 'Employee %s does not exists' % name

def update_emp(name):
    emp = Emp_Collection.query.filter(Emp_Collection.name==name).first()
    if emp:
        choice = raw_input('Do you want to modify it? y/n : ')
        if choice in ('y','Y'):
            print 'Employee name: %s , Email : %s' % (emp.name,emp.email)
            emp.email = raw_input('Enter the Email to modify : ')
            emp.save()
            print 'Employee %s modified' % (emp.name)
        elif choice in ('n','N'):
            print 'Employee name: %s , Email : %s' % (emp.name,emp.email)
        else:
            print 'Invalid choice'

print 'Enter your choice :\n1 : Add Employee\n2 : Update Employee\n3 : Delete Employee:\n4 : To display all employees'
choice = raw_input()
if choice == '1':
    get_emp(raw_input('Enter the Employee name to add : '))
elif choice == '2':
    update_emp(raw_input('Enter the Employee name to update : '))
elif choice =='3':
    delete_emp(raw_input('Enter the Employee name to delete : '))
elif choice =='4':
    get_emps()
else:
    print 'Invalid choice'