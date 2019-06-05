import redis

#	配置信息
class Config(object):
	DEBUG = True

	SECRET_KEY = "ASKLqwy219$%^&-+123"

	#	mysql连接
	SQLALCHEMY_DATABASE_URI = 'mysql://root:123123@127.0.0.1:3306/ihome'
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	#	redis
	REDIS_HOST = '127.0.0.1'
	REDIS_PORT = 6379

	#	flask-session配置
	SESSION_TYPE = 'redis'
	SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
	SESSION_USE_SIGNER = True	#	对cookie中session_id进行隐藏
	PERMANENT_SESSION_LIFETIME = 86400	#	session数据的有效期 单位秒，有效一天


class DevelopmentConfig(Config):
	"""开发模式"""
	pass

class ProductionConfig(Config):
	"""生产环境"""
	DEBUG = False

config_map = {
	'develop':DevelopmentConfig,
	'product':ProductionConfig
}
