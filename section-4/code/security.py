from user import User

#Avoid string compare with '=='
from werkzeug.security import safe_str_cmp 

# users = [
# 	{
# 		'id':1,
# 		'username':'bob',
# 		'password':'asdf'
# 	}
# ]

users = [
	User(1,'bob','asdf')
]

# username_mapping = {
# 	'bob':{
# 		'id':1,
# 		'username':'bob',
# 		'password':'asdf'
# 	}
# }

# userid_mapping = {
# 	1 :{
# 		'id':1,
# 		'username':'bob',
# 		'password':'asdf'
# 	}
# }

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id :u for u in users}

print(username_mapping.get('bob','None'))



#authenticate finds a matching user in our users list
def authenticate(username, password):
	user = username_mapping.get(username, None)
#	if user and user.password == password:
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	user_id = payload['identity']
	return userid_mapping.get(user_id, None)

'''
Q & A
    Q: what does identity do? 
    A: It returns a number so we can get the key to the userid_mapping and it matches username_mapping

    Q: What is in payload?
    A: the payload contains the data encoded in the JWT—which by default is just the user ID.
	A: A payload is contents of the JWT token we gonna extracts the user id from that payload once we have user id we can retrieve specfic user that matchs the payload

	Q: How did JWT knew the right ID value?
    A: That's part of Flask-JWT code by default it uses the id  attribute of the object we give it.


'''