import json
import os
import re
import base64
import datetime
import mistune
import html2text
import dbconn
import dbutil
from contextlib import suppress
from hashlib import md5
from steem.blockchain import Blockchain

class Article:
    subject = ""
    content = ""
    author = ""
    preview = ""
    url = ""
    tag = []
    img = None
    hashId = ""
    created = None
    

def run():
    conn = dbutil.getConnection()
    b = Blockchain()
    for block in b.stream_from(full_blocks=True):
        print(block['block_id'])
        btxs = list(map(lambda x:x['operations'][0], block['transactions']))
        for tx in btxs:
            if tx[0] == 'comment' and tx[1]['parent_author'] == '':
                meta = json.loads(tx[1]['json_metadata'])
                print(meta['tags'])
                #if "kr" in meta['tags']:
                article = Article()
                article.author = tx[1]['author']
                article.subject = tx[1]['title']
                article.content = tx[1]['body']
                article.tag = meta['tags']
                html = mistune.markdown(article.content)
                text = html2text.html2text(html)
                article.preview = text[0:100]
                article.hashId = base64.b64encode(md5(article.preview.encode("UTF-8")).digest())[0:32]
                article.created = datetime.datetime.strptime(block['timestamp'], '%Y-%m-%dT%H:%M:%S')
                article.url = "https://steemkr.com/@" + article.author + "/" + tx[1]['permlink']
                if "image" in meta:
                    article.img = meta['image']
                if article.content.startswith("@@ ", ) == False:
                    print("upload to db")
    
if __name__ == '__main__':
    run()