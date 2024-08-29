'''Create a binary file with roll number, name and marks. Input a roll number and update the
marks.'''
import pickle as p
def writedata():
    a=[]
    f=open('stud.dat','wb')
    while True:
        b={}
        roll=int(input('enter the roll number: '))
        name=input('Enter a Name: ')
        mark=int(input('enter marks: '))
        b['roll no']=roll
        b['name']=name
        b['marks']=mark
        a.append(b)
        ch=input("do you want to try again: ")
        if ch in 'Nn':
            break
    p.dump(a,f)
    f.close()
def editdata():
    f=open('stud.dat','rb')
    lis=[]
    data=p.load(f)
    lis=data
    f.close()
    se=int(input('enter the roll no of the student you want to edit the marks of: '))
    print(lis)
    for i in lis:
        if i['roll no']==se:
            ch=int(input('Enter the new marks: '))
            print(i)
            i['marks']=ch
            print(i)
    f=open('stud.dat','wb')
    p.dump(lis,f)
writedata()
editdata()