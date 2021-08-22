import psycopg2

postgres_ip = '172.24.0.2'

connection = psycopg2.connect(f"host={postgres_ip} port=5432 dbname=admin user=admin password=admin")
cur = connection.cursor()
cur.execute("select * from work_users")
for row in cur:
    print(row)

