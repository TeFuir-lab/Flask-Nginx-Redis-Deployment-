from flask import Flask
import pymysql
import redis

app = Flask(__name__)

#MariaDB 连接
def get_conn():
    return pymysql.connect(
            host='127.0.0.1',
            user='dev',
            password='123456',
            database='devops'
    )

# Redis 连接
r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

@app.route('/add/<name>')
def add_user(name):
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
        #写入后删除缓存
        r.delete('user_list')

        return f"添加成功: {name}"
    except Exception as e:
        return str(e)
@app.route('/list')
def list_users():
    try:
        #先查Redis
        cache = r.get('user_list')
        if cache:
            return f"缓存数据：{cache}"
        #没缓存 -》查数据库
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return str(cursor.fetchall())
        
        #写入缓存（60秒后过期）
        r.set('user_list', str(data), ex=60)

        return f"数据库数据：{data}"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
