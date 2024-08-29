'''Create a binary file with roll number, name and marks. Search for a given roll number and
display the name, if not found display appropriate message.'''
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
def finddata():
    f=open('stud.dat','rb')
    dap=p.load(f)
    se=int(input('enter the roll no you are searching for:'))
    for i in dap:
        if i['roll no']==se:
            print(i['name'])
        else:
            print('there is no student of given roll number')
writedata()
finddata()