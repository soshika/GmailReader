import redis

class REDIS:
    host = 'localhost'
    port = 6379
    db = 0
    r = redis.Redis()

    def __init__(self, *args, **kwargs):
        self.r = redis.Redis(host=self.host, port=self.port, db=self.db)
    