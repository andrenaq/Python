# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:31:11 2018

@author: andre
"""
import pymysql
import pymysql.cursors
conn = pymysql.connect('localhost','root','','Emplyee')
cur = conn.cursor()
cur.execute("Select VERSION()")
data1=cur.fetchone()
print("Database version: %s" % data1)
conn.close()
#2
conn = pymysql.connect('localhost','root','','Emplyee')
cur = conn.cursor()
cur.execute("drop table if exists employee")
sql=""" CREATE TABLE employee ( first_name char(20) not null
    , last_name char(20)
    , age int
    , gender char(1)
    , salary float)"""
try:
    cur.execute(sql)
    conn.commit()
except:
    conn.rollback()
conn.close()
# 3
conn = pymysql.connect('localhost','root','','Emplyee')
cur = conn.cursor()
sql="""
    insert into employee (first_name, last_name, age, gender, salary)
    values('mac','Mohan',20,'m',2000),('jan','Lucy',40,'F',2555)
"""
try:
    cur.execute(sql)
    conn.commit()
except:
    conn.rollback()
conn.close()
#4  
conn = pymysql.connect('localhost','root','','Emplyee')
cur = conn.cursor()
sql=""" 
    select * from employee where salary >'%d'
"""%(1000)
try:
    cur.execute(sql)
    resultset=cur.fetchall()
    count=cur.rowcount
    print(resultset,count)
    for row in resultset:
            fname=row[0]
            lname=row[1]
            age=row[2]
            gen=row[3]
            sal=row[4]
            print('fname=%s,lname=%s,age=%d,gen=%s,sal=%d' % (fname,lname,age,gen,sal))
except:
    print('Erro: unable to fetch data')
conn.close()
#5
conn = pymysql.connect('localhost','root','','twitter')
cur = conn.cursor()
sql="update employee set salaray=salary+100 where gender =%c"%('M')
try:
    cur.execute(sql)
    conn.commit()
except:
    conn.rollback()

conn.close()
#6
conn = pymysql.connect('localhost','root','','twitter')
cur = conn.cursor()
sql="""delete from employee where first_name='%s' """%('Tim')
try:
    cur.execute(sql)
    conn.commit()
except:
    conn.rollback()
conn.close()

