import mysql.connector
import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def check(email):

    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, email)):
        print("Valid Email")
        return 1

    else:
        print("Invalid Email")
        return 0

mydb=mysql.connector.connect(
    host="localhost",
    user="aya",
    password="test@1234",
    database="python"
)

cur= mydb.cursor()
cur.execute('''create table if not exists  employee(
            id int primary key not null auto_increment,
            full_name text not null,
            money int , 
            sleepmood char(20),
            healthrate char(20),
            email char(20),
            workmood char(20),
            salary int,
            is_manager int
            
            );''')
#cur.execute('''drop table employee;''')
mydb.commit()

class Person:
    def __init__(self,full_name,money,hours,meals):
        self.full_name=full_name
        self.money=money
        self.sleep(hours)
        self.eat(meals)

    def sleep(self,hours):
        if int(hours)==7:
            self.sleepmood="happy"
        elif int(hours)<7:
            self.sleepmood="tired"
        else:
            self.sleepmood="lazy"    
    def eat(self,meals):
            if int(meals)==3:
                self.healthRate=100
            elif int(meals)== 2:
                self.healthRate=75
            elif int(meals)== 1:
                self.healthRate=50


    def buy(self,items):
        self.money-=10*items


class Employee(Person):
    def __init__(self,email,salary,is_manager,full_name,money,workhours,sleephours,meals):
        Person.__init__(self,full_name,money,sleephours,meals)
        self.email=email
        self.salary=salary
        self.is_manager=is_manager
        self.work(workhours)


    def work(self,hours):
        if int(hours)==8:
            self.workmood="happy"
        elif int(hours)<8:
            self.workmood="tired"
        else:
            self.workmood="lazy"    
    
    @classmethod    
    def sendEmail(cls,sender_name,subject,body,receiver_name):
        f = open("email.txt", "w+")
        f.write(" To: "+ receiver_name +"\n From: "+ sender_name+"\n Subject: "+subject+"\n"+body)
        f.close()

class Office:
    office_name="Alex HQ"
    employees=[]

    @classmethod
    def get_all_employees(cls):
        cur.execute('select * from employee')
        Office.employees= cur.fetchall()
        mydb.commit()
        return Office.employees
    
    @classmethod   
    def get_employee(cls,empId):
        return Office.emplyees[empId]
    def hire(employee):
        cur.execute(' insert into employee(full_name,money,sleepmood,healthrate,email,workmood,salary,is_manager)\
        values("'+employee.full_name+'",'+employee.money+',"'+employee.sleepmood+'","'\
        +str(employee.healthRate)+'","'+employee.email+'","'+employee.workmood+'",'+employee.salary+','+employee.is_manager+'); ')
        mydb.commit()
    def fire(empId):
        cur.execute('delete from employee where id='+empId+';')
        mydb.commit()

while True:
    print('''Welcome to our office system  
            \nselect a number from 1 to 3  
            \n1- Hire new Employee
            \n2- Fire an Employee  
            \n3- get all employees
            \n4- Quit''')

    choice=input("Enter your choice: ")
    if choice == "4":
        mydb.close()
        break
    elif choice=="3":
        print(Office.get_all_employees())
    elif choice=="2":
        empId=input("Enter Employee Id you want to remove: ")
        Office.fire(empId)    
    elif choice=="1":
            is_manager="0"
            print('''
            1- manager \n 
            2- normal \n 
            ''')

            ch=input("Enter your choice: ")
            if ch==1:
                is_manager="1"
            
            full_name=input(">>Name: ")
            while True:
                email=input(">>Email: ")
                if check(email):
                    break
                else:
                    print("you entered invalid email, try again")
            while True:
                salary=input(">>Salary: ")
                if int(salary)>1000:
                    break
                else:
                    print("Salary must be 1000 or more, try again")
            money=input(">>Money: ")
            workhours=input(">>Number of work hours: ")
            sleephours=input(">>Number of sleep hours: ")
            meals=input(">Number of meals(1-2-3): ")

            emp =Employee(email,salary,is_manager,full_name,money,workhours,sleephours,meals)
            Office.hire(emp)
    else:
    print("Invalid Choice")


Employee.sendEmail("aya@gm","test send email method"," dear everybody \n this is a hello message from aya hussein","everybody@gm")

