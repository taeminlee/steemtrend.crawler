# steemtrend.crawler

The crawler used by steemtrend.com

## Virtual Env (Optional)

`pip install virtualenv`
`virtualenv -p python3.5 venv`
`. venv/bin/activate`

## Installation

`pip install steem pymysql mistune html2text`
`copy dbconn.py.sample dbconn.py`
edit dbconn.py

## Run

`python crawl.py`
