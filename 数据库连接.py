import pymysql
db=pymysql.connect(host='192.168.88.100',port=3306,user='root',password='123456',database='test')#创建数据库对象
cursor=db.cursor()#创建游标对象
cursor.execute('drop table if exists stutu')#此处可添加sql语句
cursor.close()#关闭游标
print('finish')
db.close()#关闭数据库