import psycopg2

# Connection information
postgres_ip = '172.18.0.4'
port = '5432'
db_name = 'admin'
user_name = 'admin'
password = 'admin'

try:
    connection = psycopg2.connect(f"host={postgres_ip} port={port} dbname={db_name} user={user_name} password={password}")
    cur = connection.cursor()
    cur.execute("select * from work_users")
    for row in cur:
        print(row)

except Exception as e:
    print(f"\nDB接続に失敗しました。　[接続先: {postgres_ip}:{port}]")
    print("-"*80)
    print("<エラーメッセージ>")
    print(e)

