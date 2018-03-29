from flask import Flask
from user import User

app = Flask(__name__)




if __name__ == "__main__":
	api.add_resource(UserRegister, '/register')
	app.run(port=8080)