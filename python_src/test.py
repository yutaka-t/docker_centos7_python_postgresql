import psycopg2

# Connection information
postgres_ip = '172.19.0.2'
port = '5432'
db_name = 'admin'
user_name = 'admin'
password = 'admin'


connection = psycopg2.connect(f"host={postgres_ip} port={port} dbname={db_name} user={user_name} password={password}")
cur = connection.cursor()
cur.execute("select * from work_users")
for row in cur:
    print(row)

