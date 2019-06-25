

BOT_NAME = 'fangtianxia'
SPIDER_MODULES = ['fang.spiders']
NEWSPIDER_MODULE = 'fang.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 0.25


DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

ITEM_PIPELINES = {
   # 'fang.pipelines.FangPipeline': 300,
   'fang.pipelines.MongoPipeline': 400,
    'fang.pipelines.MysqlTwistedPipline': 420,
}

DOWNLOADER_MIDDLEWARES = {
    'fang.middlewares.UserAgent': 300,
}

# 1、确保request存储到redis中
#SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"

# 2、确保所有爬虫共享相同的去重指纹
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"

# 3、在redis中保持scrapy-redis用到的队列，不会清理redis中的队列，从而可以实现暂停和恢复的功能。
SCHEDULER_PERSIST = True

# 4、Redis URL建立redis数据连接
REDIS_URL = 'redis://:Re_Lei@127.0.0.1:6379'

# 5、散列函数的个数（k），默认为6个
BLOOMFILTER_HASH_NUMBER = 6

# 6、Bloom Filter的Bit参数，默认30，占用128MB空间，去重量级1亿
BLOOMFILTER_BIT = 10


# B、建立MongoDB连接
MONGO_URI = '139.155.96.221'
MONGO_DB = 'fangtianxia'
#在CentOs下写入数据需要使用账号密码连接
MONGO_USERNAME = 'root'
MONGO_PASSWORD = 'Mongo_Lei'
# MONGO_URL = 'mongodb://root:123456@192.168.43.68:27017'

# C、建立MySQL连接
MYSQL_HOST = '139.155.96.221'
MYSQL_DATABASE = 'fangtianxia'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Sql_Lei'

