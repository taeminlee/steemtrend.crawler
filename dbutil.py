import pymysql.cursors

def get_last_blockId(conn):
    with conn.cursors as cursor:
        sql = "SELECT id from maaum_news_st_block ORDER BY timestamp desc limit 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]

def insert_blockId(conn, id, timestamp):
    with conn.cursors as cursor:
        sql = "INSERT INTO maaum_news_st_block (id, timestamp) VALUES (%s, %s)"
        cursor.execute(sql, (id, str(timestamp)))
    conn.commit()