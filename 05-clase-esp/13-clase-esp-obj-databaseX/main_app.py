from database_x import DatabaseX

database = DatabaseX()

# sql = (
#     "INSERT INTO `cardexdb`.`client`(`id`,`name`,`age`,`email`) "
#     + f"VALUES(0,'test',23,'test@test.com');"
# )
# database.executeNonQueryBool(sql)

# sql2 = (
#     "UPDATE `cardexdb`.`client` "
#     + f"SET `name` = 'testx', `age` = 25,`email` = 'testx@testx.com' "
#     + f"WHERE `id` = 7;"
# )
# rows = database.executeNonQueryRows(sql2)
# if rows > 0:
#     print("query executed correctly")
# else:
#     print("something went wrong")

data = database.executeQueryRows("SELECT * FROM cardexdb.client;")
# print(data)
for row in data:
    print(row["id"], row["name"])
database.endConnection()

database.startConnection()
data = database.executeQueryRows("SELECT * FROM cardexdb.client;")
for row in data:
    print(row["age"], row["email"])
database.endConnection()

database.startConnection()
data = database.executeQueryOneRow("SELECT * FROM cardexdb.client where id=2;")
print(data["id"], data["name"], data["age"])
database.endConnection()
