import pymysql

db = pymysql.connect(host='localhost',user='root',password='hyyldlbhs.1314',port=3306,db='spiders')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print("DATABASE version",data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')

# sql = 'create table if not exists students (id varchar(255) not null, name varchar(255) not null,age int not null, primary key(id))'
# cursor.execute(sql)

# idd = '2012001'
# user = 'Bob'
# age = 20
# sql = 'insert into students(id,name,age) values({}, {}, {})'


# ===============插入数据===================
# data = {
#     'id': '2012002',
#     'name': 'Bob',
#     'age': 20
#     }
# table = 'students'
# keys = data.keys()
# keys = ', '.join(keys)
# leb = ['%s'] * len(data)
# values = ', '.join(['%s'] * len(data))
# sql = 'insert into {table}({keys}) values({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback() #如果异常则数据回滚
# db.close()

# ================更新数据===================
# sql = 'update students set age = %s where name = %s'
# try:
#     cursor.execute(sql,(25,'Bob'))
#     db.commit()
# except:
#     db.rollback()


# data = {
#     'id': '20120001',
#     'name': 'Bob',
#     'age': '21'
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))

# sql = 'insert into {}({}) values({}) on duplicate key update'.format(table,keys,values)
# update = ','.join([" {} = %s".format(key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql,tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#================查询数据====================
sql ='select * from students where age >= 20'
try:
    cursor.execute(sql)
    print('Count: ',cursor.rowcount)
    one = cursor.fetchone() #得到结果的第一条数据
    print('One: ',one)
    results = cursor.fetchall() #得到所有数据
    print('Results: ',results)
    print('Results Type: ',type(results))
    for row in results:
        print(row)
except:
    print('Error')