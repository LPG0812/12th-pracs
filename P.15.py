Stack=[]
def PUSH():
    while True:
        a={}
        pin=int(input('Enter the pin code of the city: '))
        name=input('Enter the name of the city: ')
        a['pin']=pin
        a['name']=name
        Stack.append(a)
        ch=input('Do you want to push another node?: ')
        if ch in 'Nn':
            break
    menu()
def POP():
    if len(Stack)==0:
        print("stack is empty")
    else:
        print(Stack.pop(),'is removed')
    menu()
def Disp():
    if len(Stack)==0:
        print("stack is empty")
    else:
        for i in range(len(Stack)-1,-1,-1):
            print(Stack[i])
    menu()
def menu():
    while True:
        opt=int(input('''
1. PUSH() to push a node into the stack.
2. POP() to remove a node from the stack.
3. Display the stack.
4. Exit.
Which of the following options you want to try?: '''))
        if opt==1:
            PUSH()
        if opt==2:
            POP()
        if opt==3:
            Disp()
        else:
            break
menu()        
