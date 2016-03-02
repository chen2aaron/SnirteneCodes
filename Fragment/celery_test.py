import requests
from celery_config import app


@app.task()
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)

def main(urls):
    for url in urls:
        fetch_url.delay(url)

if __name__ == '__main__':
    urls = ['https://baidu.com', 'http://douban.com', 'http://weibo.com', 'http://zhihu.com', 'http://bing.com']
    main(urls)
