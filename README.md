# 4567tv增量式爬虫

# 原理：
redis set去重
![Image text](https://github.com/fenghuoxiguozu/4567tv/blob/master/img/redis.png)

如果要将节目标题内容作为标识，可用hash存储
con=Redis(host='127.0.0.1',port=6379)
data=hashlib.sha256(content.encode()).hexdigest()
ex=self.con.sadd('data',data)

# Redis数据存储
![Image text](https://github.com/fenghuoxiguozu/4567tv/blob/master/img/pipeline.png)
