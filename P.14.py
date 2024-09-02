'''Develop a Python program which stores employee number,
name and salary of employees in
“employee.csv”, calculates and
display the total salary remitted to the employees
and to display the
number of employees who are drawing
a salary of more than Rs. 15,000/- per month.'''
import csv
def enterdata():
    with open('employees.csv','w',newline='') as f:
        rec=csv.writer(f,delimiter=',')
        rec.writerow(['employee num','name','salary'])
        while True:
            num=int(input('Enter the employee number: '))
            name=input('Enter the name: ')
            sal=int(input('Enter the salary: '))
            rec.writerow([num,name,sal])
            ch=input('Do you want to try again: ')
            if ch in 'Nn':
                break
        print("The file is created.")
def totsal():
    with open('employees.csv','r') as f:
        rea=csv.reader(f)
        tot=0
        co=0
        for i in rea:
            if rea.line_num==1:
                continue
            tot+=int(i[2])
            if int(i[2])>15000:
                co+=1
    print('Total salary remitted is:',tot)
    print('Number of employees whose salary is more than 15,000:',co)        
enterdata()
totsal()
