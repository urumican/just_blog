class Config(object):
	"""Base config class."""
	pass

class ProdConfig(Config):
	"""Production config class.""" 
	pass 

class DevConfig(Config): 
	"""Development config class.""" 
	# Open the DEBUG 
	DEBUG = True

	# MySQL connection
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fanguiju@127.0.0.1:3306/jmilkfansblog'
