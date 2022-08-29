import pymysql
db=pymysql.connect(host="localhost",user="root",passwd="232523",db="database1")
cur=db.cursor()
sql="select * from student4"
cur.execute(sql)
# a=cur.fetchall()                                     #fetchall=print all
print("the number of rows=",cur.rowcount)              #fetchone=print single record
# if a:                                                #cur.rowcount  print the number of rows
    # print(a[0],"  ",a[1])
# db.commit()
db.close()