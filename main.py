
import psycopg2 as sql

db = sql.connect(
    database='autosalon',
    host='localhost',
    user='postgres',
    password='Instagram'
)

cursor = db.cursor()

##============== 1 ====================

# cursor.execute('''select model_id, model_name, model_price, brand_name, color_name, car_count from models
# join colors on colors.color_id = models.color_id
# join brands on brands.brand_id = models.brand_id
# ''')
# models = cursor.fetchall()
# print('='*84)
# print("|", "ID".center(5, " "), "|", "MODEL NAME".center(22, " "), "|", "PRICE".center(10, " "), "|",
#       "BRAND".center(13, " "), "|", "COLOUR".center(10, " "), "|", "COUNT".center(5, " "), "|")
# print('='*84)
# for i in models:
#     print("|", str(i[0]).center(5, " "), "|", i[1].center(22, " "), "|", str(i[2]).center(10, " "), "|", i[3].center(13, " "),"|", i[4].center(10, " "),"|", str(i[5]).center(5, " "),"|")
#     print('-'*84)
#


##=============== 2 ========================

# cursor.execute("""
# select email from employees
# union
# select email from customers
# """)
# emails = cursor.fetchall()
# print('='*29)
# print("|", "EMAILS".center(25, " "), "|")
# print('='*29)
# for i in emails:
#     print("|", i[0].center(25, " "),"|")
#     print('-' * 29)


##========== 3 ==================

# cursor.execute('''
# select country, count(customer_id) from customers
# group by country
# order by count(customer_id)
# ''')
# country_count = cursor.fetchall()
# print('='*25)
# print("|", "COUNTRY".center(13, " "), "|", "COUNT".center(5, " "), "|")
# print('='*25)
# for i in country_count:
#     print("|",i[0].center(13, " "),"|",str(i[1]).center(5, " "),"|")
#     print('-' * 25)


##================ 4 ==========================

# cursor.execute('''
# select country, count(employee_id) from employees
# group by country
# order by count(employee_id)
# ''')
# country_count = cursor.fetchall()
# print('='*25)
# print("|", "COUNTRY".center(13, " "), "|", "COUNT".center(5, " "), "|")
# print('='*25)
# for i in country_count:
#     print("|",i[0].center(13, " "),"|",str(i[1]).center(5, " "),"|")
#     print('-' * 25)


##================== 5 ====================

# cursor.execute('''
# select brand_name, count(model_id) from models
# join brands on brands.brand_id = models.brand_id
# group by brand_name
# order by count(model_id)
# ''')
# brands = cursor.fetchall()
# print('='*25)
# print("|", "BRAND".center(13, " "), "|", "CARS".center(5, " "), "|")
# print('='*25)
# for i in brands:
#     print("|",i[0].center(13, " "),"|",str(i[1]).center(5, " "),"|")
#     print('-' * 25)



##============= 6 ===================

# cursor.execute('''
# select brand_name, count(model_id) from models
# join brands on brands.brand_id = models.brand_id
# group by brand_name
# having count(model_id) > 5
# order by count(model_id)
# ''')
# brands = cursor.fetchall()
# print('='*25)
# print("|", "BRAND".center(13, " "), "|", "CARS".center(5, " "), "|")
# print('='*25)
# for i in brands:
#     print("|",i[0].center(13, " "),"|",str(i[1]).center(5, " "),"|")
#     print('-' * 25)


##============== 7 =====================

# cursor.execute('''
# select order_id, customers.first_name ||' '|| customers.last_name as customers_name,
# employees.first_name ||' '|| employees.last_name as employees_name, model_name, model_price,
# models.car_count, order_date from orders
# join customers on customers.customer_id = orders.customer_id
# join employees on employees.employee_id = orders.employee_id
# join models on models.model_id = orders.model_id
# ''')
# orders = cursor.fetchall()
# print('='*117)
# print("|", "ORDER ID".center(5, " "), "|", "CUSTOMER".center(22, " "), "|", "EMPLOYEE".center(13, " "), "|",
#       "MODEL".center(22, " "), "|", "PRICE".center(10, " "), "|", "COUNT".center(5, " "), "|", "ORDER DATE".center(15, " "), "|")
# print('='*117)
# for i in orders:
#     print("|", str(i[0]).center(8, " "), "|", i[1].center(22, " "), "|", str(i[2]).center(10, " "), "|", i[3].center(22, " "),"|", str(i[4]).center(10, " "),"|", str(i[5]).center(5, " "),"|", str(i[6]).center(15, " "), "|")
#     print('-'*117)


##============ 8 ================

# cursor.execute('''
# select sum(model_price) from models
# ''')
# price = cursor.fetchone()
# for i in price:
#     print(i)


##============= 9 ===================

cursor.execute('''
select count(brand_id) from brands
''')
brand = cursor.fetchone()
for i in brand:
    print(i)

db.commit()
db.close()