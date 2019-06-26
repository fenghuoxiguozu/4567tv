# 4567tv增量式爬虫

# 去重方法
将爬取过程中产生的url进行存储，存储在redis的set中。当下次进行数据爬取时，首先对即将要发起的请求对应的url在存储的url的set中做判断，如果存在则不进行请求，否则才进行请求。
对爬取到的网页内容进行唯一标识的制定，然后将该唯一表示存储至redis的set中。当下次爬取到网页数据的时候，在进行持久化存储之前，首先可以先判断该数据的唯一标识在redis的set中是否存在，在决定是否进行持久化存储。
![Image text](https://github.com/fenghuoxiguozu/4567tv/blob/master/img/redis.png)

如果要将节目标题内容作为标识，可用hash存储
con=Redis(host='127.0.0.1',port=6379)
data=hashlib.sha256(content.encode()).hexdigest()
ex=self.con.sadd('data',data)

# Redis数据存储
![Image text](https://github.com/fenghuoxiguozu/4567tv/blob/master/img/pipeline.png)
