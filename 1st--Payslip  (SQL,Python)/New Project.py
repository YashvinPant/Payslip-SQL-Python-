import mysql.connector
from tabulate import tabulate
import pandas as pd
import numpy as np

print('# PAYSLIP GENRATING SYSTEM')
print()
print()
a=input('Name:-')
print('Departments-IT, Finance, Marketing, Production, Purchasing, etc')
c=input('Your Department:-')
d=input('Your ID:-')
m=input('Month:-')
print()
print()
print("# YOUR PAYSLIP FOR MONTH",m.upper(),"IS :-")

mydb=mysql.connector.connect(host='localhost',\
                             user='root',\
                             passwd='1234',\
                             database='project3')

#  p=Basic Pay, q=HRA, w=DA, ma=Medical Allowance, t= All Taxes(PF,CTS,GSLI), pf=Total Pay
if c =='IT':
    p=70000
    q=3500
    w=2000
    ma=2500
    t=4000
    pf=p+q+w+ma-t
elif c =='Finance':
    p=30000
    q=3500
    w=2000
    ma=2500
    t=4000
    pf=p+q+w+ma-t
elif c =='Marketing':
    p=35000
    q=3500
    w=2000
    ma=2500
    t=4000
    pf=p+q+w+ma-t
elif c =='Production':
    p=30000
    q=3500
    w=2000
    ma=2500
    t=4000
    pf=p+q+w+ma-t
elif c =='Purchasing':
    p=25000
    q=3500
    w=2000
    ma=2500
    t=4000
    pf=p+q+w+ma-t
else:
     p=30000
     q=3500
     w=2000
     ma=2500
     t=4000
     pf=p+q+w+ma-t
import mysql.connector
mycursor=mydb.cursor()
l="insert into payslip2 values"
y=(d,a,c,m,p,q,w,ma,t,pf)
j=(f'{l}{y}')
mycursor.execute(j)
mydb.commit()
j1='select ID,Name,Department,Month,Basic_Pay,HRA,DA,MA,ALL_Taxes,Total_Pay from payslip2 where ID='
k=j1+d
mycursor.execute(k)
results=mycursor.fetchall()
print(tabulate(results, headers=['ID', 'Name','Department','Month','Basic_Pay','HRA','DA','MA','ALL_Taxes',',Total_Pay'], tablefmt='psql'))
print()
print('Your Total Salary for month',m.upper(),'is:-',pf,'/-')




