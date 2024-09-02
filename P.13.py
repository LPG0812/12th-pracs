'''Write a menu driven program implementing user-defined functions on a CSV file “students” to
read and display the name and percentage of the records of students.'''
import csv
def enterdata():
    with open('student.csv','w',newline='') as f:
        rec=csv.writer(f,delimiter=',')
        rec.writerow(['admissionno','name','percentage'])
        while True:
            ad=input('Enter the admission number: ')
            name=input('Enter the name: ')
            per=input('Enter the percentage: ')
            rec.writerow([ad,name,per])
            ch=input('Do you want to enter more data(Y/N): ')
            if ch in 'Nn':
                break
        print('The file is created')
    menu()
def readdata():
    with open('student.csv','r') as f:
        rec1=csv.reader(f)
        for i in rec1:
            if rec1.line_num==1:
                continue
            print('Name:',i[1],'Percentage:',i[2])
    menu()
def menu():
    op=int(input('''
1. Enter the information of students.
2. Display the information of the students.
Which option you want to choose: '''))
    if op==1:
        enterdata()
    if op==2:
        readdata()
menu()
    

