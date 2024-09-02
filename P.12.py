'''Create a CSV file by entering user-id and password, read and search the password for given
userid.'''
import csv
def enterdata():
    with open('user.csv','w',newline='') as f:
        info=csv.writer(f,delimiter=',')
        info.writerow(['user','id'])
        while True:
            use=int(input('Enter the user id: '))
            pas=int(input('Enter the password: '))
            info.writerow([use,pas])
            ch=input('Do you want to try again: ')
            if ch in 'Nn':
                break
    print('The file is created.')
def findata():
    se=int(input('Enter the user id you are searching for: '))
    with open('user.csv','r') as f:
        info1=csv.reader(f)
        flag=0
        for i in info1:
            if i[0]==str(se):
                print('password of given id is:',i[1])
                flag=1
        if flag==0:
            print('There is no password of given id.')
enterdata()
findata()
    
        
    
    
