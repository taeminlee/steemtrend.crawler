import pymysql.cursors

def get_last_blockId(conn):
    with conn.cursor() as cursor:
        sql = "SELECT id from maaum_news_st_block ORDER BY id desc limit 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            return 14267112 # 14267112 / 2017.08.4
        return int(result['id'])

def insert_blockId(conn, id, timestamp):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO maaum_news_st_block (id, timestamp) VALUES (%s, %s)"
            cursor.execute(sql, (id, str(timestamp)))
        conn.commit()
    except:
        pass

def insert_article(conn, article):
    nno = 0
    with conn.cursor() as cursor:
        sql = "INSERT INTO `maaum_news_st`(`url`, `title`, `press`, `gcat`, `gcid`, `img`, `description`, `created_at`, `update_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (article.url, article.subject, article.author, article.hashId, article.hashId, article.img, article.text, article.created, article.created))
        nno = cursor.lastrowid
    with conn.cursor() as cursor:
        sql = "INSERT INTO `maaum_news_st_raw`(`nno`, `md`, `tags`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nno, article.content, str(article.tag)))
    conn.commit()
