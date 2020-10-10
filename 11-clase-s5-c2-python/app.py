# como conectarnos a Mysql
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="sakila",
    cursorclass=pymysql.cursors.DictCursor,
)

mycursor = connection.cursor()

sql = "SELECT * FROM sakila.country;"

mycursor.execute(sql)
result = mycursor.fetchall()
# print(result)

for row in result:
    print(row["country"])
