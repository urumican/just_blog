from flask_sqlalchemy import SQLAlchemy
from main import app
from uuid import uuid4

db = SQLAlchemy(app)

class User(db.Model):
	"""Represents Proected users."""

	# Set the name for table 
	__tablename__ = 'users' 
	id = db.Column(db.String(45), primary_key=True) 
	username = db.Column(db.String(255)) 
	password = db.Column(db.String(255))
	
	def __init__(self, username, id, password):
		self.username = username
		self.id = id
		self.password = password

	def __repr__(self):
		return "<Model User `{}`>".format(self.username)

class Role(db.Model):
	__tablename__ = 'roles'

	id = db.Column(db.String(45), primary_key=True)
	name = db.Column(db.String(255), unique=True)
	description = db.Column(db.String(255))

	def __init__(self):
		self.id = str(uuid4())

	def __repr__(self):
		return "<Model Role `{}`>".format(self.name)
		
class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.String(45), primary_key=True)
	title = db.Column(db.String(255))
	text = db.Column(db.Text())
	publish_date = db.Column(db.DateTime)

	user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
	
	# one to many
	user = db.relationship('User', back_populates='posts')
