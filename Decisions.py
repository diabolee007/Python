answer=input('Are you sure you want to exit the program?\n')
if answer=='yes':
    print('bye bye!')
else:
    print('thanks for staying around!')

Status=input('Enter you work status:\n')
Age=int(input('Enter you age:\n'))
if not (Status =="Retired" or Age>60):
    print('You are not a senior citizen')
else:
    print('you are a senior citizen')


username = input('Enter username:\n')
password = input('Enter password:\n')
if username =='admin' and password =='p4s$':
    print('Acces Granted')
else:
    print('Access Denied')
    
