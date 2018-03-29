from user import User

#Avoid string compare with '=='
from werkzeug.security import safe_str_cmp 

users = [
	User(1,'bob','asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id :u for u in users}

print(username_mapping.get('bob','None'))


# userid_mapping = {
# 	1 :{
# 		'id':1,
# 		'username':'bob',
# 		'password':'asdf'
# 	}
# }

def authenticate(username, password):
	user = username_mapping.get(username, None)
#	if user and user.password == password:
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	user_id = payload['identity']
	return userid_mapping.get(user_id, None)


