from PIL.ImagePalette import random
from numpy.random import randint


# Exercise 1
print('-------------------Exercise 1-------------------')
print('Hello World')
user_name=input('please write your name here: ')
print('Nice to meet you {}'.format(user_name))

# Exercise 2
print('-------------------Exercise 2-------------------')
a,b=map(lambda x:float(x),input('Please write two numbers like: 7,8 (float is acceptable): ').split(','))
print('Sum:',a+b)
print('Difference:',a-b)
print('Product:',a*b)
print('Quotient:',a/b)

# Exercise 3
print('-------------------Exercise 3-------------------')
temperature=float(input('Please write the temperature: '))
type=input('''Please tell if it's Celsius or Fahrenheit (just write 'C' or 'F'): ''' )
print('Celsius: {}\nFahrenheit: {}'.format(temperature if type=='C' else round((temperature-32)/1.8,2) , temperature if type =='F' else round(32+temperature*1.82,2)))

# Exercise 4
print('-------------------Exercise 4-------------------')
number_guess=randint(1,101)
count_time=0
while count_time<7:
    count_time+=1
    print('{} times left'.format(7-count_time))
    number=int(input('give your number: '))
    if number==number_guess:
        print('Correct!')
        print('You win!')
        break
    elif number>number_guess:
        print("Too high!")
    else:
        print('Too low!')

# Exercise 5
print('-------------------Exercise 5-------------------')
list_used=[4, 7, 10, 2, 8, 5, 1, 9, 3, 6]
print('The smallest number:',sorted(list_used)[0])
print('The largest number:',sorted(list_used)[-1])
print('The sum of all numbers:',sum(list_used))
print('The average (mean) of all numbers',sum(list_used)/len(list_used))
print('a new list with only the even numbers:',[i for i in list_used if i%2==0])

# Exercise 6
print('-------------------Exercise 6-------------------')
list_exercise6=input('please write a sentence here:').lower().split()
dict_exercise6={}
set_exercise6=set(list_exercise6)
for i_exercise6 in set_exercise6:
    dict_exercise6[i_exercise6]=list_exercise6.count(i_exercise6)
print(dict_exercise6)

# Exercise 7
print('-------------------Exercise 7-------------------')
password=input('please give your password here:')
print('At least 8 characters long:','OK' if len(password)>=8 else 'Not OK')
print('Contains at least one uppercase letter:','OK' if len([i for i in password if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])>0 else 'Not OK' )
print('Contains at least one lowercase letter:','OK' if len([i for i in password if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()])>0 else 'Not OK' )
print('Contains at least one number:','OK' if len([i for i in password if i in '0123456789'])>0 else 'Not OK' )

# Exercise 8
print('-------------------Exercise 8-------------------')
shoplise_exercise8=[]
while True:
    order_exercise8=input('please choose a option:[ Add, Remove, Show, Clear, Exit]:')
    if order_exercise8 not in [ 'Add', 'Remove', 'Show', 'Clear', 'Exit'] :
        print('Please choose the right option!')
    elif order_exercise8=='Add':
        shoplise_exercise8.append(input('give a item here:'))
        print('your shopping list:','\n','\n'.join(shoplise_exercise8) )
    elif order_exercise8=='Remove':
        item_remove=input('give a item here:')
        if item_remove not in shoplise_exercise8:
            print('''item doesn't exsist''')
            continue
        shoplise_exercise8.remove(item_remove)
        print('your shopping list:', '\n', '\n'.join(shoplise_exercise8))
    elif order_exercise8=='Show':
        print('your shopping list:', '\n', '\n'.join(shoplise_exercise8))
    elif order_exercise8=='Clear':
        shoplise_exercise8=[]
    elif order_exercise8=='Exit':
        print('Your shopping journey is ended!')
        break

# Exercise 9
print('-------------------Exercise 9-------------------')
Q1_exercise9=input('''\n1+1=()
A.2    B.3
C.4    D.5
give you answer here:''')
Q2_exercise9=input('''\n11+11=()
A.22    B.33
C.44    D.55
give you answer here:''')
Q3_exercise9=input('''\n111+111=()
A.222    B.333
C.444    D.555
give you answer here:''')
score_exercise9=[i for i in (Q1_exercise9,Q2_exercise9,Q3_exercise9) if i=='A'or i=='a']
print('\nyour final score is:',len(score_exercise9)*10,'/30')

# Exercise 10
print('-------------------Exercise 10-------------------')
with open('diary.txt','w',encoding='utf-8') as f:
    list_to_write_exercise10=[]
    print('please write what you did today')
    while True:
        string_exercise10=input()+'\n'
        if string_exercise10=='\n':
            break
        list_to_write_exercise10.append(string_exercise10)
    f.writelines(list_to_write_exercise10)

with open('diary.txt','r',encoding='utf-8') as f:
    file_exercise10=f.read()
    print('the contents of this file:')
    print(file_exercise10)
