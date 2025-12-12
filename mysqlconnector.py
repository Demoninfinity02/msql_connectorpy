import tkinter as t
win=t.Tk()

from time import sleep
def tome(a,t=0.000000000000125):
    for i in a:
        print(i,end='')
        sleep(t)
    print()
def choice():
    tome('===================================================WELCOME==============================================================',0.00000000125)
    tome('                               1.SHOW ALL DATABASES '                                                           )
    tome('                               2.CREATE NEW DATABASE'                                                             )
    tome('                               3.OPEN THE DATABASE'                                                             )
    tome('                               4.SHOW ALL TABLES')
    tome('                               5.CREATE NEW TABLE '                                                                 ) 
    tome('                               6.DISPLAY THE RECORDS OF THE TABLE'                                                             )
    tome('                               7.INSERT A NEW RECORD IN THE SELECTED TABLE'                                        )
    tome('                               8.DROP THE TABLE')
    tome('                               9.DESCRIBE THE SELECTED TABLE')
    tome('                               10.ADD PRIMARY KEY')
    tome('                              11.DROP THE PRIMARY KEY')
    tome('                              12.DROP THE FOREIGN KEY')
    tome('                              13.ADD THE FOREIGN KEY')
    tome('                              14.UPDATE ANY  RECORD FROM A  TABLE')
    tome('                              15.UPDATE ANY COLUMN NAME')
    tome('                              16.DELETE  ANY RECORD FROM TABLE')
    tome('                              17.DELETE ANY COLUMN FROM TABLE')
    tome('                              18.EXIT THE PROGRAM')
    tome('========================================================================================================================',0.00000000125)
    import mysql.connector as p
    cn=p.connect(host='localhost',user='root',password='password')#use your mysql password here in the password section
    cr=cn.cursor()
        
    while True:
            try:
                n=int(input('enter the choice number:-'))
                if n==1:
                    z="show databases;"
                    cr.execute(z)
                    d=cr.fetchall()
                    print(d)
                elif n==2:
                    i=input('enter the new database name=') 
                    z="create database {};".format(i)
                    print(z)
                    cr.execute(z)
                    cn.commit()
                elif n==3:
                    i=input('Enter the database name=')
                    z="use {};".format(i)
                    print(z)
                    cr.execute(z)
                    print('connection established')    
                elif n==5:
                    i=input('enter the table name:-')
                    a=int(input('enter the number of fields required:-'))
                    z="create table "+ i+'('
                    for k in range(a-1):
                        n1=input('enter the field name=')
                        n2=input('enter the field type=')
                        n3=input('enter the field size=')
                        if n3=='0':
                            n3=None
                            c=n1+' '+n2+','
                            z=z+c
                        else:
                            c=n1+' '+n2+'('+n3+'),'
                            z=z+c
                    else:
                        n1=input('enter the field name=')
                        n2=input('enter the field type=')
                        n3=input('enter the field size=')
                        if n3=='0':
                            n3=None
                            c=n1+' '+n2+');'
                            z=z+c
                        else:
                            c=n1+' '+n2+'('+n3+'));'
                            z=z+c
                    print(z)
                    cr.execute(z)
                    cn.commit()
                elif n==6:
                    i=input('enter the table name:-')
                    z="select * from {};".format(i)
                    cr.execute(z)
                    d=cr.fetchall()
                    print(d)
                elif n==7:
                    n4=input('Enter the table name:-')
                    z="desc {};".format(n4)
                    cr.execute(z)
                    d=cr.fetchall()
                    print(d)
                    a=len(d)
                    n5=''
                    for k in range(a):
                        n1=input('enter the field value=')
                        
                        n5=n5+n1+','
                        print(n5)
                    n3='insert into {} values('.format(n4)+n5.rstrip(',')+')'
                    print(n3)
                    cr.execute(n3) 
                elif n==8:
                    n1=input('Enter the table name:-')
                    q="drop table {};".format(n1)
                    cr.execute(q)
                    d=cr.fetchall()
                    for k in range(len(d)):
                        print(d[k])
                elif n==9:
                    n2=input('Enter the table name:-')
                    z="desc {};".format(n2)
                    cr.execute(z)
                    d=cr.fetchall()
                    print(d)
                elif n==10:
                    n1=input('Enter the table name:-')
                    n2=input('Enter the field to be make it primary key:-')
                    z="alter table {} add primary key({});".format(n1,n2)
                    print(z)
                    cr.execute(z)
                    cn.commit()
                elif n==11:
                    n1=input('Enter the table name:-')
                    z=("alter table {} drop primary key;").format(n1)
                    cr.execute(z)
                    cn.commit()    
                elif n==18:
                    print('Thank u')
                    break
                elif n==12:
                    n1=input('enter table name')
                    z=("alter table {} drop foreign key constraint=`{}_ibfk_1`;").format(n1,n1)
                    cr.execute(z)
                    d=cr.fetchall()
                    print(d)
                    cn.commit()
                elif n==13:
                    n1=input('enter table name')
                    n2=input('enter the reference table name')
                    n3=input('enter the field name to made it foreign key;-')
                    n4=input('enter the field name of the reference table;-')
                    z=("ater table {} add foreign key({}) references {}({});").format(n1,n2,n3,n4)
                    cr.execute(z)
                    cn.commit()
                elif n==14:
                    n1=input('enter table name')
                    n2=input('enter the field name to be updated')
                    n3=input('enter the  new field value')
                    n4=input('enter the reference field name  ')
                    n5=input('enter the reference field value')         
                    z="update {} set {}={} where {}={};".format(n1,n2,n3,n4,n5)
                    cr.execute(z)
                    cn.commit()
                elif n==16:
                    n1=input('enter table name')
                    n2=input('enter the reference field name ')
                    n3=input('enter the  reference field value')
                    z='delete from {}  where {}={}'.format(n1,n2,n3)
                    cr.execute(z)
                    cn.commit()
                elif n==15:
                    n1=input('enter table name')
                    n2=input('enter the  field name ')
                    n3=input('enter the  new field name')
                    n4=input('enter the new field data type')
                    z='ALTER TABLE {} CHANGE {} {} {};'.format(n1,n2,n3,n4)
                    cr.execute(z)
                    cn.commit()
                elif n==17:
                    n1=input('enter table name')
                    n2=input('enter the  field name to be deleted ')
                    z='ALTER table {} drop {};'.format(n1,n2)
                    cr.execute(z)
                    cn.commit()
                elif n==4:
                    z='show tables;'
                    print(z)
                    cr.execute(z)
                    d=cr.fetchall()
                    print(d)
                    cn.commit()
                else:
                    print('incorrect choice')
                    print('thank u')
                    break
            except:
                       print('incorrect entry')
                       continue


    

def MAIN():
        pwd=e.get()
        if pwd=='password':#enter your password 
                win.destroy()
                choice()
        else:
            win.destroy()
            print('incorrect pwd')
disp=t.Label(text='WELCOME TO THE PROJECT PLEASE ENTER THE PASSWORD',bg="red", fg="white")
disp.pack()
e=t.Entry(text='enter password',show='*',bg='white', fg="black")
e.place(x=685, y=100, width=180, height=60)
b=t.Button(text='SUBMIT',command=MAIN)
b.pack()
win.geometry('1200x960')
win.mainloop() 




    
